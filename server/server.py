# -*- coding: utf-8 -*-
import sys
import socket
import ssl

class Binder(object):
    def __init__(self,host,port,max_client_num,cert_file):
        self.host=host
        self.port=port
        self.max_client_num=max_client_num
        self.cert_file=cert_file
        self.start()
    def start(self):
        pass
    def stop(self):
        pass

if __name__ == '__main__':
    import configparser
    config = configparser.ConfigParser()
    if(len(sys.argv))<2:
        config_name='default.ini'
    else:
        config_name=sys.argv[1]
    if(len(sys.argv))<3:
        config_section='default'
    else:
        config_section=sys.argv[2]
    config.read(config_name)
    cf = config[config_section]
    #print(config_name)
    binder=Binder(cf['host'],int(cf['port']),int(cf['max_client_num']),cf['cert_file'])