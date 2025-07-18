#!PATH_TO_YOUR_PYTHON
import subprocess
import json
import os
import sys
import npyscreen

EDITOR = str(os.environ.get("EDITOR", "nvim"))
CONFIG_PATH = "PATH_TO_YOUR_CONFIG.json"

with open(CONFIG_PATH, "r") as file:
    data = json.load(file)

# def saveall():
#     subprocess.Popen([
#     "python3",
#     "/home/seva/git/backup/my_configs/main.py"
# ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def GetSelection(*args):
    form = npyscreen.Form(name='Config Manager')
    myForm = form.add(npyscreen.TitleSelectOne, name='Config to manage', values=list(data.keys()))
    form.edit()
    return myForm.value


if len(sys.argv) < 2:

    selection = npyscreen.wrapper_basic(GetSelection)[0]

    arg = list(data.keys())[selection]
else:
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
