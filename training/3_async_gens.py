import socket
from select import select
tasks = []

to_read = {}
to_write = {}

def server():
    my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    my_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    my_socket.bind(('localhost', 6000))
    my_socket.listen()

    while True:

        print('мы находимся перед ассепт')
        yield ('read',my_socket)
        client_sock,adrs_cliend = my_socket.accept()
        print('Входяшие подключение',adrs_cliend)
        tasks.append(client(client_sock))

def client(client_sock):
    while True:
        yield ('read', client_sock)
        request = client_sock.recv(4096)

        if not request:
            break
        else :
            response = 'Hello World\n'.encode()
            yield ('write', client_sock)
            client_sock.send(response)

    print('вне внутренего цикла вайл')
    client_sock.close()


def event_loop():
    while any([tasks,to_read,to_write]):

        while not tasks:
            ready_to_read,ready_to_write,_ = select(to_read,to_write,[])
            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task =  tasks.pop(0)

            reason,sock = next(task)
            if reason == 'read':
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task
        except StopIteration:
            print('Done!')



tasks.append(server())
event_loop()