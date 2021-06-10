import server
import threading
import tools

my_server = server.Server(
    ('', 8282),
    5,
)

my_server.start()

while True:
    client, *_ = my_server.accept()
    threading.Thread(target=tools.talk_with_client, args=(client, my_server.commands_list,)).start()