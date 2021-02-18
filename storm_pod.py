#!/usr/bin/python3

# Base Imports
import argparse
import os
import shutil
import json
import urllib.request

# Custom Code
from bin.utils.argument_controller import argument_controller
from bin.utils.configuration_controller import config_controller
from bin.server_controller import create_game_server


app_settings = {}
# Grabs path where this script was ran.
script_dir = os.path.dirname(os.path.abspath(__file__))
prefix_dir = os.path.abspath(os.path.join(script_dir))

# =============== Arguments =============================
args = argument_controller()
# =============== Arguments =============================

# ================ Configuration Piece ===================
config_settings = config_controller(script_dir, "var/conf/default.conf", "var/conf/local.conf")
app_name = config_settings.get('general', 'app_name')
version = config_settings.get('general', 'version')
description = config_settings.get('general', 'description')
app_settings["app_name"] = config_settings.get('general', 'app_name')
app_settings["version"] = config_settings.get('general', 'version')
app_settings["description"] = config_settings.get('general', 'description')
app_settings["docker_image"] = config_settings.get('docker', 'image')
app_settings["app_dir"] = prefix_dir


# ================ Configuration Piece ===================

print("Welcome to {}".format(app_name))
print(description)
print("<{}>".format(version))
print("========================================================")
print("")

if args.install:
    print("Installing Dockerfile: {1}/var/lib/docker/{0}/Dockerfile".format(app_settings["docker_image"], app_settings["app_dir"]))
    print("--------------------------------------------------------")
    command = "docker build -t storm-pod:latest . -f {1}/var/lib/docker/{0}/Dockerfile".format(app_settings["docker_image"], app_settings["app_dir"])
    os.system(command)
    print("Docker Image Installed: {}:latest".format(app_settings["docker_image"]))


if args.create and args.create is not None:
    print("Creating Docker Container")
    print("--------------------------------------------------------")
    user_input = args.create
    create_game_server(app_settings, user_input)

if args.list:
    print("Game Server Containers List")
    print("If you just installed me, and I don't have any game servers the --install will set me up.")
    print("Make sure to run --update to get latest game list.")
    print("--------------------------------------------------------")
    data = urllib.request.urlopen("https://raw.githubusercontent.com/thegreatstorm/ansiblepods/main/gamelist.txt")
    for line in data:
        print(line)

if args.update:
    print("Updating Scripts")
    print("--------------------------------------------------------")
    print("Currently working on it.")
