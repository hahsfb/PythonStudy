from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime


HOST = ""
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from:', self.client_address)
        data = '[%s] %s' % (ctime(), self.rfile.readline().decode('utf-8'))
        print('============================================================')
        print(data, end='')
        print('============================================================')
        self.wfile.write(data.encode())


tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection....')
tcpServ.serve_forever()
