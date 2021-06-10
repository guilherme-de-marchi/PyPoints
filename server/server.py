import socket
import tools

class Server(socket.socket):
    def __init__(self, address: tuple, max_connections: int):
        tools.assert_type(address, tuple)
        tools.assert_type(max_connections, int)

        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.address, self.max_connections = address, max_connections
        self.commands_list = {
            'help': self.help_command
        }

    def start(self):
        tools.debug_print(self.address)
        self.bind(self.address)
        self.listen(self.max_connections)

    def stop(self):
        self.shutdown()
        self.close()

    def help_command(self) -> str:
        return '''
        I'm helping you   : )
        '''