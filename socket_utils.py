import socket


def socket_create_server(host=socket.gethostname(), port=12345):
    sock = socket.socket()
    HOST = host
    PORT = port
    try:
        sock.bind((HOST, PORT))
        return sock
    except ConnectionRefusedError:
        print("Connection refused...")
        exit(0)


def socket_create_client(host=socket.gethostname(), port=12345):
    sock = socket.socket()
    HOST = host
    PORT = port
    try:
        sock.connect((HOST, PORT))
        return sock
    except ConnectionRefusedError:
        print("Connection refused...")
        exit(0)


def socket_push(sock, m):
    sock.send(m)


def socket_recv(sock):
    return sock.recv(1024)


def socket_close(sock):
    sock.close()


def socket_accept(sock):
    return sock.accept()
