import deviceMgmt
import threading
import time
import traceback

"""
Main program

Read present micros, configure and start the tests as indicated (parameters?)

""" 

deviceMgmt.findArduinos()

# test
time.sleep(1)
try:
    uin = input()
    while uin != "":
        deviceMgmt.microList[0].write( uin +"\n")
        while True:
            try:
                print(deviceMgmt.microList[0].read(1000))
            except:
                break;
        uin = input();
    
except Exception as e:
    traceback.print_exc()


# Trigger destructor call
del deviceMgmt.microList
