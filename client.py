import argparse
from socket_utils import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, help="specify a port number \
        (defaults to 12345)")
    parser.add_argument('-m', '--message', type=str, help="specify a \
        message to send")
    args = parser.parse_args()
    p = args.port if args.port else 12345
    m = args.message if args.message else b'PING'
    sock = socket_create_client(socket.gethostname(), p)
    socket_push(sock, m)
    print("received message", socket_recv(sock).decode("utf-8"))
    socket_close(sock)
