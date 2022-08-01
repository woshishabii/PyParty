import unittest
import socket
import sys

class TestConnectionV1(unittest.TestCase):
    def test_connect(self):
        address = ('0.0.0.0', 9999)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(address)
            sock.sendall(bytes('hello\n', 'utf-8'))
            received1 = str(sock.recv(1024), 'utf-8')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(address)
            sock.sendall(bytes('world\n', 'utf-8'))
            received2 = str(sock.recv(1024), 'utf-8')
        self.assertEqual(received1, 'HELLO')
        self.assertEqual(received2, 'WORLD')

if __name__ == '__main__':
    unittest.main()