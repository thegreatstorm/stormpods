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
from bin.server_controller import Servers


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
    server = Servers(app_settings=app_settings, user_input=user_input)
    server.create()

if args.delete and args.delete is not None:
    user_input = args.delete
    print("Deleting Docker Container: {}".format(user_input))
    print("--------------------------------------------------------")
    server = Servers(container_id=user_input)
    server.delete()

if args.list:
    print("Game Server Containers List")
    print("Make sure you keep me updated do a git pull!")
    print("--------------------------------------------------------")
    game_list = ""
    data = urllib.request.urlopen("https://raw.githubusercontent.com/thegreatstorm/ansiblepods/main/gamelist.txt")
    for line in data:
        game_list = line.decode('utf-8').split(',')

    for game in game_list:
        print(game)

