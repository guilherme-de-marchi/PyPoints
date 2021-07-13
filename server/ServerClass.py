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

        self.logged_clients = {}

        self.bind(self.address)
        self.listen(self.max_connections)

    def stop(self):
        self.shutdown()
        self.close()

    def send_data(self, message: str, targets: tuple):
        tools.assert_type(message, str)
        tools.assert_type(targets, tuple)
        tools.for_each(targets, lambda item: tools.assert_type(item, ClientClass.Client))

        message = message.encode()
        tools.for_each(targets, lambda client: client.socket.send(message))

    def talk_with(self, client_socket):
        client = ClientClass.NotLoggedClient(client_socket, self.commands_list)
        tools.debug_print(f'New connection from -> {client.socket}')

        while True:
            received_data = client.socket.recv(1024).decode()
            tools.debug_print(f'Data received from -> {client.socket} :: {received_data}')
            received_data = received_data[:-2] + ' ' #Formating !fix this!

            current_command = received_data.split(' ', 1)
            current_command = {
                'name': current_command[0],
                'args': current_command[1].split(' '),
            }
            
            tools.debug_print(current_command)
            
            if client.verify_command_access(current_command['name']):
                self.commands_list[current_command['name']](client, *current_command['args'])

    def ping_command(self, client, *args):
        self.send_data('Pong', (client,))

    def list_command(self, client, *args):
        self.send_data(f'{self.logged_clients}', (client,))

    def register_command(self, client, *args):
        name = args[0]

        if name in self.logged_clients.keys():
            self.send_data('This name is already playing!', (client,))
            return
        
        client.change_class(ClientClass.LoggedClient)
        self.logged_clients[name] = client

        self.send_data('Registered!', (client,))