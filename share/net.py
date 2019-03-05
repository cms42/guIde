#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
sys.path.append("../xugu")
sys.path.append("../share")

import socket

class net_client_sync:
    """
    simple network client
    """
    def __init__(self):
        pass
    def send_recv(self,addr,data):
        """
        addr=(host,port)
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect(addr)
        s.send(data.encode('utf-8'))
        gd=s.recv(1024)
        s.close()
        return gd