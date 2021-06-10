import server
import tools

class Client:
    def __init__(self, socket, server_commands_list: dict):
        tools.assert_type(server_commands_list, dict)

        self.socket = socket
        self.allowed_commands = {
            'help': server_commands_list['help'],
            #'quit': server.Server.quitCommand,
        }

    def verify_command_access(self, command_name) -> bool:
        tools.assert_type(command_name, str)
        
        return command_name in self.allowed_commands.keys()

class NotLoggedClient(Client):
    def __init__(self, socket, server_commands_list: dict):
        super().__init__(socket, server_commands_list)

class LoggedClient(Client):
    def __init__(self, socket, server_commands_list: dict):
        super().__init__(socket, server_commands_list)

        #self.allowed_commands['update_position'] = server.Server.updatePositionCommand
        #self.allowed_commands['list'] = server.Server.listCommand