import argparse
import socket
from color_utils import *


class Server(object):
    # The following may be useful, `ps -fA | grep python`
    def __init__(self, host, port, protocol='tcp'):
        self.peers = []
        self.online = False
        self.protocol = protocol
        sock = socket.socket()
        HOST = host
        PORT = port
        try:
            sock.bind((HOST, PORT))
            self.sock = sock
            self.online = True
        except ConnectionRefusedError:
            print("Connection refused...")
            exit(0)

    def listen(self, limit=5):
        assert(self.online)
        message = "..."
        self.sock.listen(limit)
        while True:
            c = None
            print("Listening...")
            try:
                c, addr = self.sock.accept()
                gprint("Got connection from", addr)
                message = ret_msg(c)
                response = self.process(message)
                self.respond(c, response)
                c.close()
            # except ConnectionRefusedError:
            #     rprint("Connection refused...")
            except KeyboardInterrupt:
                rprint("\nKeyboardInterrupt...\nSocket closed.")
                if c:
                    c.close()
                break

    def process(self, m):
        if m == 'PING':
            return 'PONG'
        else:
            return 'hello, World!'

    def respond(self, sock, m):
        assert(type(m) == str)
        bprint("Sending message: ", m)
        sock.send(m.encode())

    def ret_msg(self, sock):
        assert(self.online)
        message = sock.recv(1024).decode('utf-8')
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
    args = parser.parse_args()
    p = args.port if args.port else 12345
    sock = Server(socket.gethostname(), p)
    sock.listen()
    sock.close()
