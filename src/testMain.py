''' 
-----------------------------------------------------------
Test Executor for the I4S performance testRun - Main module

Created May, 13, 2021
(C) 2017-2021 Hofer Florian, Bolzano, ITALY
Released under GNU Public License (GPL)
email info@florianhofer.it
-----------------------------------------------------------
''' 

import deviceMgmt
import testRun
import threading
import time
import traceback

endnodes = []
testers = []

#TODO: add read from file
testParameters = [{ "testRun" : 1,
                    "NodeParam" : { "mode" : 1, "chnMsk" : 0xFF, "conf" : 1, "OTAA": 0 },
                    "TestParam" : [{"mode" : 0, "freq" : 8683 },
                                   {"mode" : 0, "freq" : 8681 },
                                   {"mode" : 0, "freq" : 8685 },
                                   {"mode" : 0, "freq" : 8671 },
                                   {"mode" : 0, "freq" : 8689 },
                                   {"mode" : 0, "freq" : 8675 },
                                   {"mode" : 0, "freq" : 8677 },
                                   {"mode" : 0, "freq" : 8679 },]},
                  { "testRun" : 2,
                    "NodeParam" : { "mode" : 1, "chnMsk" : 0xFF, "conf" : 1, "OTAA": 0 },
                    "TestParam" : [{"mode" : 0, "freq" : 8683 },]},
                   ]

deviceParameters = [{   "0123456789ABCDEF" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "EUI" : {"APPEUI" : "", "APPKEY" : "" , "DEVADDR" : "", "APPSKEY": "", "NWSKEY" : ""}
                     }]

def configureTestClasses():
    '''
    create and configure testRun devices
    '''
    deviceMgmt.findArduinos()
    
    #assign to testRun instances
    for micro in deviceMgmt.microList:
        tMicro = testRun.Test(micro)
        
        if micro.EUI in deviceParameters :
            tMicro.OTAAparams(deviceParameters[micro.EUI()]["APPEUI"], deviceParameters[micro.EUI()]["APPKEY"])
            tMicro.ABPparams(deviceParameters[micro.EUI()]["DEVADDR"], deviceParameters[micro.EUI()]["APPSKEY"], deviceParameters[micro.EUI()]["NWSKEY"])
            
        if micro.type == 0:
            endnodes.append(tMicro)
        else:
            testers.append(tMicro)
        

    #TODO: sample for testRun and exclude 

def assignParams(node, params):
    for key in params:
            if key == 'mode':
                node.mode = params[key]
            elif key == 'freq': 
                node.frequency = params[key]
            elif key == 'conf': 
                node.confirmed = bool(params[key])
            elif key == 'OTAA': 
                node.otaa = bool(params[key]) 
            elif key == 'repeat': 
                node.repeatCount = params[key]
            elif key == 'chnMsk': 
                node.channelMask = params[key]
            elif key == 'power': 
                node.powerIndex = params[key]
            elif key == 'datalen': 
                node.dataLength = params[key]
            elif key == 'DR': 
                node.dataRate = params[key] 

def prepareTest(testNumber):
    '''
    Configure end and testRun nodes with the set parameters
    
    :parameter Testnumber to look for in Testparameters
    
    '''
    
    params = [x for x in testParameters if x["testRun"] == testNumber][0]    
    print ("Parameters for test:", params)

    for endnode in endnodes:
        with params["NodeParam"] as nodeParams:
            assignParams(endnode, nodeParams)                        
    
    testnodes = iter(testers)
        
    for testParms in params["TestParam"]:
        try:
            testnode = next(testnodes)
        except StopIteration:
            raise Exception ("Not enough testRun micros available")        
        
        assignParams(testnode, testParms)      

def runTest():
    print("START Test")
    for testNode in testers:
        print("RUN Test node " + str(testers.index(testNode) + 1) )
        testNode.runTest()
        
    testerThreads = []
    for testNode in testers:
        print("Threading Test node " + str(testers.index(testNode) + 1) )
        x = threading.Thread(target=testNode.poll, args = ())
        x.start()
        testerThreads.append(x)
    
    for endnode in endnodes:
        print("RUN End node " + str(endnodes.index(endnode) + 1) )
        endnode.runTest()
        endnode.poll()
    
    for testNode in testers:
        print("STOP Test node " + str(testers.index(testNode) + 1) )
        testNode.stopTest()
    
    for x in testerThreads :
        print("JOIN Test node " + str(testers.index(testNode) + 1) )
        x.join(1) 
    
    print("END Test")

"""
Main program

Read present micros, configure and start the tests as indicated (parameters?)

""" 

configureTestClasses()

prepareTest(2)

runTest()


# # testRun
# time.sleep(1)
# try:
#     uin = input()
#     while uin != "":
#         deviceMgmt.microList[0].write( uin +"\n")
#         while True:
#             try:
#                 read = deviceMgmt.microList[0].read()
#                 if read == "" :
#                     break
#                 print(read)
#             except:
#                 break;
#         uin = input();
#
# except Exception as e:
#     traceback.print_exc()


# Trigger destructor call
del deviceMgmt.microList
