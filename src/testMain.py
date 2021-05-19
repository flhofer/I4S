import deviceMgmt
import test
import threading
import time
import traceback

endnodes = []
testers = []

#TODO: add read from file
testParameters = [{ "test" : 1,
                    "NodeParam" : { "mode" : 1, "chnMsk" : 0xFF, "conf" : 1, "OTAA": 0 },
                    "TestParam" : [{"mode" : 0, "freq" : 8683 },
                                   {"mode" : 0, "freq" : 8681 },
                                   {"mode" : 0, "freq" : 8685 },
                                   {"mode" : 0, "freq" : 8671 },
                                   {"mode" : 0, "freq" : 8689 },
                                   {"mode" : 0, "freq" : 8675 },
                                   {"mode" : 0, "freq" : 8677 },
                                   {"mode" : 0, "freq" : 8679 },]},
                  { "test" : 2,
                    "NodeParam" : { "mode" : 1, "chnMsk" : 0xFF, "conf" : 1, "OTAA": 0 },
                    "TestParam" : [{"mode" : 0, "freq" : 8683 },]},
                   ]

def configureTestClasses():
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

    #Todo: sample for test and exclude

    # try:    
    #     testers[0].__writeParams()
    # except Exception as e:
    #     pass    

def prepareTest(testNumber):
    '''
    Configure end and test nodes with the set parameters
    
    :parameter Testnumber to look for in Testparameters
    
    '''
    
    params = [x for x in testParameters if x["test"] == testNumber][0]    
    print (params)

    for endnode in endnodes:
        with params["NodeParam"] as nodeParams:
            for key in nodeParams: 
                if key == 'mode':
                    endnode.mode = nodeParams[key]
                elif key == 'freq': 
                    endnode.frequency = nodeParams[key]
                elif key == 'conf': 
                    endnode.confirmed = bool(nodeParams[key])
                elif key == 'OTAA': 
                    endnode.otaa = bool(nodeParams[key])
                elif key == 'repeat': 
                    endnode.repeatCount = nodeParams[key]
                elif key == 'chnMsk': 
                    endnode.channelMask = nodeParams[key]
                elif key == 'power': 
                    endnode.powerIndex = nodeParams[key]
                elif key == 'datalen': 
                    endnode.dataLength = nodeParams[key]
                elif key == 'DR': 
                    endnode.dataRate = nodeParams[key]                                     
    
    testnodes = iter(testers)
        
    for testParms in params["TestParam"]:
        try:
            testnode = next(testnodes)
        except StopIteration:
            raise Exception ("Not enough test micros available")        
        
        for key in testParms:
            if key == 'mode':
                testnode.mode = testParms[key]
            elif key == 'freq': 
                testnode.frequency = testParms[key]
            elif key == 'conf': 
                testnode.confirmed = bool(testParms[key])
            elif key == 'OTAA': 
                testnode.otaa = bool(testParms[key]) 
            elif key == 'repeat': 
                testnode.repeatCount = testParms[key]
            elif key == 'chnMsk': 
                testnode.channelMask = testParms[key]
            elif key == 'power': 
                testnode.powerIndex = testParms[key]
            elif key == 'datalen': 
                testnode.dataLength = testParms[key]
            elif key == 'DR': 
                testnode.dataRate = testParms[key] 

def runTest():
    pass


"""
Main program

Read present micros, configure and start the tests as indicated (parameters?)

""" 

configureTestClasses()

prepareTest(2)

runTest()


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
