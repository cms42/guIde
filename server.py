# -*- coding: UTF-8 -*-
import sys
dev = False
if len(sys.argv)>1:
    for i in (range(len(sys.argv)-1)):
        if sys.argv[i+1]== '--dev':
            print('您正位于开发者模式')
            dev = True
        else:
            print '天哪！出错了！未知命令行：',sys.argv[i+1]
if not dev:
    from xugu import *
else:
    from xugu_dev import *