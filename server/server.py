# -*- coding: utf-8 -*-
import sys
import socket
import ssl
import threading

class Processor(object):
    def __init__(self):
        pass
    def process():
        pass

class Responder(threading.Thread):
    def __init__(self,client_socket,addr):
        self.client_socket=client_socket
        self.addr=addr
        threading.Thread.__init__(self)
    def run(self):
        len = self.client_socket.recv(4)
        typ = self.client_socket.recv(4)
        data = self.client_socket.recv(len)


class Binder(object):
    def __init__(self,host,port,max_client_num,certfile,keyfile):
        self.host=host
        self.port=port
        self.max_client_num=max_client_num
        self.certfile=certfile
        self.keyfile=keyfile
        self.start()
    def start(self):
        context = ssl.SSLContext()
        context.load_cert_chain(self.certfile,self.keyfile)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
            sock.bind((self.host,self.port))
            sock.listen(self.max_client_num)
            with context.wrap_socket(sock, server_side=True) as ssock:
                while True:
                    client_socket, addr = ssock.accept()
                    responder = Responder(client_socket,addr)
                    responder.start()

if __name__ == '__main__':
    import configparser
    config = configparser.ConfigParser()
    if(len(sys.argv))<2:
        config_name='default.ini'
        print('配置文件未指定，自动使用默认配置default.ini')
    else:
        config_name=sys.argv[1]
    if(len(sys.argv))<3:
        config_section='default'
        print('配置文件单元未指定，自动使用默认单元default')
    else:
        config_section=sys.argv[2]
    config.read(config_name)
    cf = config[config_section]
    #print(config_name)
    binder=Binder(cf['host'],int(cf['port']),int(cf['max_client_num']),cf['certfile'],cf['keyfile'])