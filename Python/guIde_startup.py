import runpy
import os
import threading
import time

path1='/guIde.d/server/'
path2='/guIde.d/clientA/'
startup_delay=10
delay=2

def run(path,run_name='__main__'):
    runpy.run_path(path,run_name=run_name)

if __name__ == "__main__":
    #Wait for system to start and config camera
    print("Waiting the system to startup...")
    time.sleep(startup_delay)

    path=os.getcwd()
    print("Startup from ",path)

    os.chdir(path+path1)
    t1=threading.Thread(target=run,args=('./'), name='run')
    t1.start()
    print("Waiting for the server to start...")
    time.sleep(delay)
    #wait for the server to start

    os.chdir(path+path2)
    t2=threading.Thread(target=run,args=('./',), name='run')
    t2.start()

    t1.join()
    t2.join()
