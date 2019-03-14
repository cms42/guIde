#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
sys.path.append("../xugu")
sys.path.append("../share")
import json

import db
import server

def main():
    if len(sys.argv)<2:
        config_name="config.json"
    else:
        config_name=sys.argv[2]
    config=json.load(open(config_name,'r'))
    _db=db.json_db(config["db_config"])
    _db.read()
    _server=server.server(config["server_config"],db)
    _server.start()

if __name__ == "__main__":
    main()