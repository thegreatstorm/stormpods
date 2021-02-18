import argparse


def argument_controller():
    # Plugins may have to been done manual has mods are different per game server.
    parser = argparse.ArgumentParser('Automate your Game Server\'s!')
    parser.add_argument('--create', help='Create your game server', required=False)
    parser.add_argument('--delete', help='Delete your game server', required=False)
    parser.add_argument('--update', help='Update ansible scripts, and docker image.', required=False, action='store_true')
    parser.add_argument('--install', help='Install Docker Image', required=False, action='store_true')
    parser.add_argument('--list', help='List Game Servers', required=False, action='store_true')
    args = parser.parse_args()
    return args