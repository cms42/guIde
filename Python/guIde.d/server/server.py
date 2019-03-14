#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
sys.path.append("../xugu")
sys.path.append("../share")

import socket
import db

class server:
    """
    the server
    """
    def __init__(self,config,dbcfg):
        self.config=config
        self._db=db.json_db(dbcfg)
        self._db.read()
        print(self._db.get("test:cms"))

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
            sd=self._db.get(data)
            print("发送：",sd)
            clientsocket.send(sd.encode('utf-8'))
            clientsocket.close()