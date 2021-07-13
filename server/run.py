import threading
import ServerClass

server = ServerClass.Server(
    ('', 8282),
    5,
)

server.start()

while True:
    client, *_ = server.accept()
    threading.Thread(target=server.talk_with, args=(client,)).start()