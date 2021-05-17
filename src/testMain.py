import deviceMgmt

"""
Main program

Read present micros, configure and start the tests as indicated (parameters?)

""" 

deviceMgmt.findArduinos()

# test
try:
    deviceMgmt.microList[0].write("T\n")
    
    while True:
        try:
            print(deviceMgmt.microList[0].read(100))
        except:
            break;
except:
    pass
