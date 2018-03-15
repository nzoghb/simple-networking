import argparse
import socket
from color_utils import *


class Client(object):
    def __init__(self, host, port, protocol='tcp'):
        self.online = False
        self.protocol = protocol
        sock = socket.socket()
        HOST = host
        PORT = port
        try:
            sock.connect((HOST, PORT))
            self.sock = sock
            self.online = True
        except ConnectionRefusedError:
            rprint("Connection refused...")
            exit(0)

    def push(self, m):
        assert(type(m) == str)
        bprint("Sending message: ", m)
        self.sock.send(m.encode())

    def get_msg(self):
        assert(self.online)
        message = self.sock.recv(1024).decode('utf-8')
        gprint("Received message: ", message)
        return message

    def close(self):
        assert(self.online)
        self.sock.close()
        self.online = False

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, help="specify a port number \
        (defaults to 12345)")
    parser.add_argument('-m', '--message', type=str, help="specify a \
        message to send")
    args = parser.parse_args()
    p = args.port if args.port else 12345
    m = args.message if args.message else 'PING'
    sock = Client(socket.gethostname(), p)
    sock.push(m)
    sock.get_msg()
    sock.close()
