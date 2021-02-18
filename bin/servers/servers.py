from subprocess import check_output, Popen
import socket
import threading
import os

from bin.utils.system_controller import random_port, random_password


def command_prefix(container_id, command, user):
    main_command = 'docker exec -u {0} -t {1} sh -c \'{2}\''.format(user, container_id, command)

    return main_command


def rustserver(image):
    data = {}
    game_port = random_port()
    rcon_port = random_port()
    ssh_port = random_port()
    app_port = random_port()

    command = "docker run -td -p {0}:{0}/udp -p {0}:{0}/tcp -p {1}:{1}/tcp -p {2}:{2}/tcp -p {3}:22 {4}".format(game_port, rcon_port, app_port, ssh_port, image)

    try:
        container_id = check_output(command, shell=True).decode('ascii')
        container_id = container_id.rstrip("\n")

        data["container_id"] = container_id
        data["game_port"] = game_port
        data["rcon_port"] = rcon_port
        data["app_port"] = app_port

        # Insert New Record into database.
        print(str(data))
        command = command_prefix(data["container_id"], 'echo "export server_port={}">> /etc/bashrc'.format(game_port), 'root')
        os.system(command)
        command = command_prefix(data["container_id"], 'echo "export rcon_port={}" >> /etc/bashrc'.format(rcon_port), 'root')
        os.system(command)
        command = command_prefix(data["container_id"], 'echo "export app_port={}" >> /etc/bashrc'.format(app_port), 'root')
        os.system(command)
        command = command_prefix(data["container_id"], 'echo "echo -e \"Welcome to Storm Pods! Server Port: {} Rcon Port: {} Mobile Port: {} \"" >> /etc/bashrc'.format(game_port,rcon_port,app_port), 'root')
        os.system(command)

    except Exception as e:
        print("Failed to create container: {}".format(str(e)))
        data["status"] = "Failed to create container. {}".format(str(e))

    return data


def minecraft(image):
    data = {}
    game_port = random_port()
    bedrock_port = random_port()
    rcon_port = random_port()
    ssh_port = random_port()

    game_port = "-p {0}:{0}/udp -p {0}:{0}/tcp".format(game_port)
    bedrock_port = "-p {0}:{0}/udp -p {0}:{0}/tcp".format(bedrock_port)
    rcon_port = "-p {0}:{0}/tcp".format(rcon_port)
    ssh_port = "-p {0}:22/tcp".format(ssh_port)

    command = "docker run -td {0} {1} {2} {3} {4}".format(game_port, bedrock_port, rcon_port,  ssh_port, image)

    try:
        container_id = check_output(command, shell=True).decode('ascii')
        container_id = container_id.rstrip("\n")

        data["container_id"] = container_id
        data["game_port"] = game_port
        data["rcon_port"] = rcon_port
        data["ssh_port"] = ssh_port

        # Insert New Record into database.
        print(str(data))

    except Exception as e:
        print("Failed to create container: {}".format(str(e)))
        data["status"] = "Failed to create container. {}".format(str(e))

    return data


def terraria(image):
    data = {}
    game_port = random_port()
    ssh_port = random_port()

    game_port = "-p {0}:{0}/udp -p {0}:{0}/tcp".format(game_port)
    ssh_port = "-p {0}:22/tcp".format(ssh_port)

    command = "docker run -td {0} {1} {2}".format(game_port, ssh_port, image)

    try:
        container_id = check_output(command, shell=True).decode('ascii')
        container_id = container_id.rstrip("\n")

        data["container_id"] = container_id
        data["game_port"] = game_port
        data["ssh_port"] = ssh_port

        # Insert New Record into database.
        print(str(data))

    except Exception as e:
        print("Failed to create container: {}".format(str(e)))
        data["status"] = "Failed to create container. {}".format(str(e))

    return data


def valheim(image):
    data = {}
    game_port = random_port()
    steam_port = random_port()
    ssh_port = random_port()

    game_port = "-p {0}:{0}/udp -p {0}:{0}/tcp".format(game_port)
    steam_port = "-p {0}:{0}/udp -p {0}:{0}/tcp".format(steam_port)
    ssh_port = "-p {0}:22/tcp".format(ssh_port)

    command = "docker run -td {0} {1} {2} {3}".format(game_port, steam_port, ssh_port, image)

    try:
        container_id = check_output(command, shell=True).decode('ascii')
        container_id = container_id.rstrip("\n")

        data["container_id"] = container_id
        data["game_port"] = game_port
        data["ssh_port"] = ssh_port

        # Insert New Record into database.
        print(str(data))

    except Exception as e:
        print("Failed to create container: {}".format(str(e)))
        data["status"] = "Failed to create container. {}".format(str(e))

    return data