#!/usr/bin/env python3
import subprocess
import json
import os
import sys

EDITOR = str(os.environ.get("EDITOR", "nvim"))
CONFIG_PATH = "/home/seva/projects/python/conf/data.json"

with open(CONFIG_PATH, "r") as file:
    data = json.load(file)



def saveall():
    subprocess.call([
        "/home/seva/git/backup/env/bin/python",
        "/home/seva/git/backup/main.py"
    ])


if len(sys.argv) < 2:
    print("Укажите ключ")
    sys.exit(1)

arg = sys.argv[1]
if arg == "-p" and sys.argv[2] in data:
    print(data[sys.argv[2]])
    sys.exit()
if arg == "-a":
    print(data)
    sys.exit()
if arg in data:
    filepath = data[arg]
    subprocess.call([EDITOR, filepath])
    saveall()
else:
    print("Config not found")

