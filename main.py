#!/bin/env python
import subprocess
import json
import os
import sys

EDITOR = str(os.environ.get("EDITOR", "nvim"))
CONFIG_PATH = "/home/seva/.config/scripts/config.json"
ASCII_CODES = {
    "RESET": "\033[0m",
    "BOLD": "\033[1m",
    "DIM": "\033[2m",
    "CYAN": "\033[36m",
    "YELLOW": "\033[33m",
    "GREEN": "\033[32m",
}

with open(CONFIG_PATH, "r") as file:
    data = json.load(file)


def saveall():
    pass
    )



def rewrite():
    with open(CONFIG_PATH, "w") as config:
        json.dump(data, config)


def is_enough(args, numb=0):
    if len(args) >= numb:
        return True
    else:
        help()
        exit("Not enough elements")


def edit_config(*args):
    is_enough(args, 1)
    if args[0] not in data:
        name_not_found()
    else:
        path = get_path(args[0])
        subprocess.call([EDITOR, path])
        saveall()
        if "command" in data[args[0]]:
            subprocess.call(data[args[0]]["command"])


def name_not_found():
    exit("Name not found")


def get_path(name=""):
    return data[name]["path"]


def path(*args):
    is_enough(args, 1)
    name = args[0]
    if name in data:
        print(get_path(name))
    else:
        name_not_found()


def cat(*args):
    is_enough(args, 1)
    name = args[0]
    with open(get_path(name), "r") as config:
        print(config.read())


def add_element(*args):
    is_enough(args, 2)
    conf = len(args)
    name = args[0]
    path = args[1]
    if 2 < conf < 5:
        if "=" not in args[2] or (conf > 3 and "=" not in args[3]) or conf > 4:
            help()
    if conf == 3:
        k, v = args[2].split("=", 1)
        data[name] = {"path": path, k: v}
    elif conf == 4:
        k, v = args[2].split("=", 1)
        val3 = args[3].split("=", 1)[1]

        if k == "group":
            data[name] = {"path": path, "group": v, "command": val3}
        else:
            data[name] = {"path": path, "group": val3, "command": v}
    else:
        data[name] = {"path": path}
    rewrite()
    print(f"{path} was saved as {name}")


def del_smth(*args):
    is_enough(args, 2)
    if args[0] == "name" and args[1] in data:
        print(data[args[1]]["path"] + " was removed")
        data.pop(args[1])
        rewrite()
    elif args[0] == "group":
        group = args[1]
        to_remove = []
        for i in data:
            if group == data[i]["group"]:
                to_remove.append(i)
                print(i + " will be removed")
        while True:
            ask = input(f"Remove all files in group {group}? y/N")
            if ask in ["y", "Y", "yes", "Yes", "YES"]:
                for i in to_remove:
                    data.pop(i)
                rewrite()
                exit(0)
            elif ask in ["", "n", "N", "no", "No", "NO"]:
                exit(0)
    else:
        help()

def names(*args):
    groups = {}
    no_group = []
    C = ASCII_CODES
    COLOR_GROUP = f"{C['BOLD']}{C['CYAN']}"
    COLOR_CONFIG = C["GREEN"]
    COLOR_FIELD = C["DIM"]
    RESET = C["RESET"]


    for name, config in data.items():
        group = config.get("group")
        if group is None:
            no_group.append((name, config))
        else:
            groups.setdefault(group, []).append((name, config))

    
    for name, cfg in sorted(no_group):
        print(f"{COLOR_CONFIG}• {name}{RESET}")
        if "path" in cfg:
            print(f"    {COLOR_FIELD}path: {cfg['path']}{RESET}")
        if "command" in cfg:
            print(f"    {COLOR_FIELD}command: {cfg['command']}{RESET}")

    
    for group in sorted(groups):
        print(f"{COLOR_GROUP}▼ {group}{RESET}")
        items = groups[group]
        for i, (name, cfg) in enumerate(items):
            branch = "└──" if i == len(items) - 1 else "├──"
            print(f"  {COLOR_CONFIG}{branch} {name}{RESET}")


def help(*args):
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    DIM = "\033[2m"
    GREEN = "\033[32m"

    print(f"""
{BOLD}Config Manager{RESET} — manage named config files with optional groups and commands

{BOLD}Usage:{RESET}
  {CYAN}config <name>{RESET}               {DIM}Open config in $EDITOR{RESET}
  {CYAN}config -p <name>{RESET}            {DIM}Print path to config{RESET}
  {CYAN}config -c <name>{RESET}            {DIM}Print contents of config file{RESET}
  {CYAN}config -a <name> <path>{RESET}     {DIM}Add new config{RESET}
      [key=value ...]      {DIM}(e.g. group=shells command="echo done"){RESET}

  {CYAN}config -d name <name>{RESET}       {DIM}Delete config by name{RESET}
  {CYAN}config -d group <group>{RESET}     {DIM}Delete all configs in group (with confirm){RESET}

  {CYAN}config -n{RESET}                   {DIM}Show all configs (grouped){RESET}
  {CYAN}config -h{RESET}                   {DIM}Show this help message{RESET}

{BOLD}Examples:{RESET}
  {GREEN}config -a kitty ~/.config/kitty/kitty.conf command="kill -SIGUSR1 $(pgrep kitty)"{RESET}
  {GREEN}config fish{RESET}                      {DIM}Opens config named 'fish' in your editor{RESET}
  {GREEN}config -d group shells{RESET}           {DIM}Prompts before deleting all configs in 'shells'{RESET}
""")
    exit(0)


def main():
    if len(sys.argv) < 2:
        print(
            'In future there will be TUI but now you can use only CLI, run with "-h" to get commands'
        )
    else:
        arg = sys.argv[1]
        commands = {"-p": path, "-c": cat, "-a": add_element, "-n": names, "-h": help, "--help":help}

        if arg in commands:
            commands[arg](*sys.argv[2:])
        elif arg in data:
            edit_config(arg)
        else:
            name_not_found()


if __name__ == "__main__":
    main()

