#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
sys.path.append("../xugu")
sys.path.append("../share")

import json

class json_db:
    """
    a simple database which storing data with json
    """
    def __init__(self,config):
        """
        config:a json object like
        {"db_path":"./db.json"}
        """
        self.config=config

    def read(self):
        self.db=json.load(open(self.config["db_path"],'r'))

    def get(self,key):
        try:
            ret = self.db[key]
        except Exception as e:
            ret = "DB ERROR :"+str(e)
        return ret

    def set(self,key,value):
        self.db[key]=value

    def write(self):
        json.dump(self.db,open(self.config["db_path"],'w'))