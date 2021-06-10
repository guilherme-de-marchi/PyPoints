import server

my_server = server.Server(
    ('localhost', 8888),
    5,
)

my_server.start()

while True:
    client, client_address = my_server.accept()
    