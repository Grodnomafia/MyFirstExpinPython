import socket



my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
my_socket.bind(('localhost', 6000))
my_socket.listen()

while True:
    print('мы находимся перед ассепт')
    client_sock,adrs_cliend = my_socket.accept()
    print('Входяшие подключение',adrs_cliend)

    while True:

        request = client_sock.recv(4096)

        if not request:
            break
        else :
            response = 'Hello World\n'.encode()
            client_sock.send(response)

    print('вне внутренего цикла вайл')
    client_sock.close()