import socket
from select import select

to_monitoring = []

my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
my_socket.bind(('localhost', 6000))
my_socket.listen()

def accept_connection(my_socket):
    print('мы находимся перед ассепт')
    client_sock,adrs_cliend = my_socket.accept()
    print('Входяшие подключени',adrs_cliend)
    to_monitoring.append(client_sock)

def send_messeage(client_sock):
    request = client_sock.recv(4096)
    if request:
        response = 'Hello World\n'.encode()
        client_sock.send(response)
    else:
        client_sock.close()


def event_loop():
    while True:
        ready_to_read, _ , _ = select(to_monitoring,[],[])
        for sock in ready_to_read:
            if sock is my_socket:
                accept_connection(sock)
            else:
                send_messeage(sock)


if __name__ == '__main__':
    to_monitoring.append(my_socket)
    event_loop()