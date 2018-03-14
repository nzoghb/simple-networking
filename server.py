import argparse
from socket_utils import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, help="specify a port number \
        (defaults to 12345)")
    args = parser.parse_args()
    p = args.port if args.port else 12345
    sock = socket_create_server(socket.gethostname(), p)
    sock.listen(5)
    while True:
        c = None
        print("Listening...")
        try:
            c, addr = socket_accept(sock)
            print("Got connection from", addr)
            socket_push(c, b'PONG')
        except ConnectionRefusedError:
            print("Connection refused...")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt...\nSocket closed.")
            break
        finally:
            if c:
                socket_close(c)
    socket_close(sock)

# The following may be useful, `ps -fA | grep python`
