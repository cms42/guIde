# -*- coding: UTF-8 -*-
import sys
dev = False
run_dev_hardware_test = False
if len(sys.argv)>1:
    for i in (range(len(sys.argv)-1)):
        if sys.argv[i+1]== '--dev':
            print('您正位于开发者模式')
            dev = True
        elif sys.argv[i+1]=='--run_dev_hardware_test':
            print('将在稍后运行开发硬件测试')
            run_dev_hardware_test = True
        else:
            print '天哪！出错了！未知命令行：',sys.argv[i+1]
if not dev:
    from xugu import *
else:
    from xugu_dev import *
if run_dev_hardware_test:
    print('正在运行Pin类测试：Pin(123,321,None,"开发测试")')
    pin=Pin(123,321,None,"开发测试")
    print('正在运行Pin类测试：high(),low(),on(),off()')
    pin.high()
    pin.low()
    pin.on()
    pin.off()
    print('正在运行ADC类测试：ADC(pin),read()')
    ADC = ADC(pin)
    ADC.read()
    print('正在运行DAC类测试：DAC(pin),write(123)')
    DAC = DAC(pin)
    DAC.write(123)