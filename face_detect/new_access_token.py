# -*- coding: utf-8 -*-
import urllib, sys,urllib2
import ssl

# client_id 为官网获取的AK， client_secret 为官网获取的SK
API_Key = raw_input()
SEC_Key = raw_input()
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+str(API_Key)+'&client_secret='+str(SEC_Key)
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)