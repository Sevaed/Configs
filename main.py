#!/usr/bin/env python3
import subprocess
import json
import os
import sys

EDITOR = str(os.environ.get("EDITOR", "nvim"))
CONFIG_PATH = "/home/seva/.config/scripts/config.json"

with open(CONFIG_PATH, "r") as file:
    data = json.load(file)


def saveall():
    #subprocess.call([
     #   "/home/seva/git/backup/my_configs/main.py"
    #])
    pass

if len(sys.argv) < 2:
    print("Укажите ключ")
    sys.exit(1)

arg = sys.argv[1]
if arg == "-p" and sys.argv[2] in data:
    print(data[sys.argv[2]])
    sys.exit()
if arg == "-c" and sys.argv[2] in data:
    with open(data[sys.argv[2]], "r") as config:
        print(config.read())
    sys.exit()
if arg == "-a":
    data[sys.argv[2]] = sys.argv[3]
    with open(CONFIG_PATH, "w") as config:
        json.dump(data, config)
    print(f"{sys.argv[3]} was saved as {sys.argv[2]}")
    sys.exit()
if arg == "-n":
    print(list(data.keys()))
    sys.exit()
if arg == "-h":
    print("-h for help \n-p for printing path to config file \n-n for printing all existing names for configs\n-c for using \"cat\" on file of config \n-a for adding new config {name_of_config path_to_config_file}")
    sys.exit()
if arg in data:
    filepath = data[arg]
    subprocess.call([EDITOR, filepath])
    saveall()
else:
    print("Config not found")
