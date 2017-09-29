#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(socket.INADDR_ANY, 8888)

s.listen(10)

while True:
        sock, addr = s.accept()
        t = threading.Thread(target = tcplink, args = (sock, addr))
        t.start()

def tcplink(sock, addr)
        print("Accept new connection from %s:%s..." % addr)
        sock.send(b'Welcome!')
        while True:
                data = sock.recv(1024)
                time.sleep(1)
                if not data or data.decode('utf-8') == 'exit':
                        break
                sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
        sock.close()
        print('Connection from %s:%s closed.' %s addr)
        



