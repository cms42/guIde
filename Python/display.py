import serial
import time
ser=serial.Serial("/dev/ttyS1",9600)
try:
    ser.close()
    ser.open()
except Exception:
    pass

def display_by_LCD(ser,chn,delay_time=0):
    if delay_time<=0:
        ser.write(chn.encode("GB2312"))
    else:
        for i in range(len(chn)+1):
            ser.write(chn[:i].encode("GB2312"))
            time.sleep(delay_time)

chr="测试字符串，总长度不超过50个字符进行测试。测试字符串，总长度不超过50个字符进行测试。"
display_by_LCD(ser,chr,0.5)
