from socket import *

HOST = '52.192.95.72'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('>>')
    if not data:
        break
    tcpCliSock.send(('%s\r\n' % data).encode())
    data = tcpCliSock.recv(BUFSIZ).decode('utf-8')
    if not data:
        break
    print(data.strip())
tcpCliSock.close()
