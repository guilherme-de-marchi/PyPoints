import socket
import tools

class Server(socket.socket):
    def __init__(self, address: tuple, max_connections: int):
        tools.assert_type(address, tuple)
        tools.assert_type(max_connections, int)

        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen(self.max_connections)

        self.address, self.max_connections = address, max_connections

    def start(self):
        self.bind(self.address)

    def stop(self):
        self.shutdown()
        self.close()