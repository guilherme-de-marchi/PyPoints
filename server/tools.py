import client

def debug_print(text: str):
    print(f'Debug: {text}')

def assert_type(variable, type):
    assert isinstance(variable, type), f'{variable} must be {type}'

def talk_with_client(client_socket, server_commands_list):
    my_client = client.NotLoggedClient(client_socket, server_commands_list)

    debug_print(f'New connection from -> {my_client.socket}')

    while True:
        received_data = my_client.socket.recv(1024).decode()
        debug_print(f'Data received from -> {my_client.socket} :: {received_data}')
        debug_print(f'{my_client.allowed_commands}')