import os
from bin.servers.servers import RustServer, MineCraft, Terraria, Valheim


class Servers:
    def __init__(self, app_settings, user_input, container_id):
        self.image = "storm-pod"
        self.app_settings = app_settings
        self.user_input = user_input
        self.container_id = container_id

    def create(self):
        # Image default uses.
        image = "storm-pod"

        if self.user_input == "rustserver":
            server = RustServer(image)
            server.install()
        elif self.user_input == "minecraft":
            server = MineCraft(image)
            server.install()
        elif self.user_input == "terraria":
            server = Terraria(image)
            server.install()
        elif self.user_input == "valheim":
            server = Valheim(image)
            server.install()
        else:
            print("User Input not in the list.")

    def delete(self):
        command = "docker rm -f {}".format(self.container_id)
        os.system(command)