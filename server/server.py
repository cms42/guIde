#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
sys.path.append("../xugu")
sys.path.append("../share")

import socket

class server:
    """
    the server
    """
    def __init__(self,config,db):
        self.config=config
        self.db=db

    def start(self):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host=self.config["host"]
        port=self.config["port"]
        maxc=self.config["maxconnect"]
        s.bind((host,int(port)))
        s.listen(int(maxc))
        while True:
            clientsocket,addr = s.accept()      
            print("连接地址: %s" % str(addr))
            data=clientsocket.recv(1024).decode('utf-8')
            print("接收到：",data)
            sd=self.db.get(data)
            print("发送：",sd)
            clientsocket.send(sd.encode('utf-8'))
            clientsocket.close()