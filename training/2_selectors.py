import socket
import selectors


selector = selectors.DefaultSelector()

def server():
    my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    my_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    my_socket.bind(('localhost', 6000))
    my_socket.listen()

    selector.register(fileobj=my_socket,events=selectors.EVENT_READ,data=accept_connection)

def accept_connection(my_socket):
    print('мы находимся перед ассепт')
    client_sock,adrs_cliend = my_socket.accept()
    print('Входяшие подключени',adrs_cliend)

    selector.register(fileobj=client_sock, events=selectors.EVENT_READ, data=send_messeage)


def send_messeage(client_sock):
    request = client_sock.recv(4096)
    if request:
        response = 'Hello World\n'.encode()
        client_sock.send(response)
    else:
        selector.unregister(client_sock)
        client_sock.close()


def event_loop():
    while True:
        events = selector.select()

        for key,_ in events:
            print(f"Сокет: {key.fileobj}")
            print(f"Что делать: {key.data.__name__}")
            callback = key.data
            callback(key.fileobj)



if __name__ == '__main__':
    server()
    event_loop()