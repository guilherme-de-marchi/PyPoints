import socket
import ClientClass
import tools

class Server(socket.socket):
    def __init__(self, address: tuple, max_connections: int):
        tools.assert_type(address, tuple)
        tools.assert_type(max_connections, int)

        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.address, self.max_connections = address, max_connections
        self.commands_list = {
            'ping': self.ping_command,
            'list': self.list_command,
            'register': self.register_command,
        }

    def start(self):
        tools.debug_print(self.address)

        self.logged_clients = []

        self.bind(self.address)
        self.listen(self.max_connections)

    def stop(self):
        self.shutdown()
        self.close()

    def talk_with(self, client_socket):
        client = ClientClass.NotLoggedClient(client_socket, self.commands_list)
        tools.debug_print(f'New connection from -> {client.socket}')

        while True:
            received_data = client.socket.recv(1024).decode()
            tools.debug_print(f'Data received from -> {client.socket} :: {received_data}')

            current_command = received_data.split(' ', 1)
            current_command = {
                'name': current_command[0],
                'args': current_command[1].split(' '),
            }
            
            if client.verify_command_access(current_command['name']):
                self.commands_list[current_command['name']](client, *current_command['args'])

    def ping_command(self, client, *args):
        message = 'Pong'.encode()
        client.socket.send(message)

    def list_command(self, client, *args):
        message = f'{self.logged_clients}'.encode()
        client.socket.send(message)

    def register_command(self, client, *args):
        name = args[0]

        if name not in self.logged_clients:
            self.logged_clients.append(name)

        message = 'Registered with success!'.encode()
        client.socket.send(message)