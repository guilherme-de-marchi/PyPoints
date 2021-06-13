import tools

class Client:
    def __init__(self, socket, server_commands_list: dict):
        tools.assert_type(server_commands_list, dict)

        self.socket = socket
        self.server_commands = server_commands_list
        self.allowed_commands = [
            'ping',
            'list',
        ]

    def verify_command_access(self, command_name) -> bool:
        tools.assert_type(command_name, str)
        
        return command_name in self.allowed_commands

    def change_class(self, class_target):
        self.__class__ = class_target
        self.__init__(self.socket, self.server_commands)


class NotLoggedClient(Client):
    def __init__(self, socket, server_commands_list: dict):
        super().__init__(socket, server_commands_list)

        self.allowed_commands += [
            'register',
        ]


class LoggedClient(Client):
    def __init__(self, socket, server_commands_list: dict):
        super().__init__(socket, server_commands_list)

        #self.allowed_commands += []