#!/usr/bin/env python3
import subprocess
import json
import argparse
import os

EDITOR = str(os.environ.get("EDITOR","nvim"))
CONFIG_PATH = "/home/seva/.config/scripts/config.json"

parser = argparse.ArgumentParser()
parser.add_argument("name",type=str, nargs="?",help="name of your config file")
parser.add_argument("-c","--cat",action="store_true" ,help="printing text from your's config file")
parser.add_argument("-p","--path",action="store_true",help="printing path to your's config file")
parser.add_argument("-a","--add",nargs=1,help="adding new name+path pair into config.json, you need to use")
parser.add_argument("-n","--names",action="store_true",help="printing all names for your's config files")
args = parser.parse_args()

data = {}
if os.path.isfile(CONFIG_PATH):
    with open(CONFIG_PATH, "r") as file:
        data=json.load(file)
else:
    print("Make sure that path to the file is correct and directories existing, do you want to create an empty file for configs? \n[y/n]")
    choice = input()
    if choice == "y":
        with open(CONFIG_PATH, "w"):
            pass
        print(f"file was create in {CONFIG_PATH}")
    else:
        exit()

def saveall():
    subprocess.call([
    "/home/seva/git/backup/my_configs/main.py"
])

def wrong():
    print("This name is wrong/you not provide any name, use -n flag to check which names you have, use -a to add new name+path pairs")

if args.cat and args.name in data:
    with open(data[args.name],"r") as config:
        print(config.read())
    exit()
elif args.cat:
    wrong()

if args.path and args.name in data:
    print(data[args.name])
    exit()
elif args.path:
    wrong()

if args.add:
    data[args.add[0]]=args.name
    with open(CONFIG_PATH, "w") as config:
        json.dump(data, config)
    print(f"{args.name} was saved as {args.add[0]}")
    exit()

if args.names:
    print(list(data.keys()))
    exit()

if args.name in data:
    filepath = data[args.name]
    subprocess.call([EDITOR, filepath])
    #saveall()
else:
    wrong()
