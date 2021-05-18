import deviceMgmt
import test
import threading
import time
import traceback



endnodes = []
testers = []

def configureTests():
    '''
    create and configure test devices
    '''
    deviceMgmt.findArduinos()
    
    #assign to test instances
    for micro in deviceMgmt.microList:
        if micro.type == 0:
            endnodes.append(test.Test(micro))
        else:
            testers.append(test.Test(micro))

"""
Main program

Read present micros, configure and start the tests as indicated (parameters?)

""" 

# test
time.sleep(1)
try:
    uin = input()
    while uin != "":
        deviceMgmt.microList[0].write( uin +"\n")
        while True:
            try:
                read = deviceMgmt.microList[0].read()
                if read == "" :
                    break
                print(read)
            except:
                break;
        uin = input();
    
except Exception as e:
    traceback.print_exc()


# Trigger destructor call
del deviceMgmt.microList
