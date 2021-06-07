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
import sys, getopt

#Hardware configurations
endnodes = []
testers = []

#TODO: add read from file
testParameters = [{ "testRun" : "A1",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1, "OTAA": 0 },
                    "TestParam" : [{"mode" : 1, "freq" : 8683 },
                                   {"mode" : 1, "freq" : 8681 },
                                   {"mode" : 1, "freq" : 8685 },
                                   {"mode" : 1, "freq" : 8671 },
                                   {"mode" : 1, "freq" : 8689 },
                                   {"mode" : 1, "freq" : 8675 },
                                   {"mode" : 1, "freq" : 8677 },
                                   {"mode" : 1, "freq" : 8679 },]},
                  { "testRun" : "A2",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1, "OTAA": 0 },
                    "TestParam" : [{"mode" : 1, "freq" : 8683 },]},
                   ]

deviceParameters = [{   "0123456789ABCDEF" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a30372e6008" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a303933660b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a303925650b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a3037277e08" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                     }]

def configureTestClasses():
    '''
    create and configure testRun devices
    '''
    deviceMgmt.findArduinos()
    
    i=0
    j=0
    #assign to testRun instances
    for micro in deviceMgmt.microList:
        tMicro = testRun.Test(micro, j)
        
        if micro.EUI in deviceParameters :
            tMicro.OTAAparams(deviceParameters[micro.EUI()]["APPEUI"], deviceParameters[micro.EUI()]["APPKEY"])
            tMicro.ABPparams(deviceParameters[micro.EUI()]["DEVADDR"], deviceParameters[micro.EUI()]["APPSKEY"], deviceParameters[micro.EUI()]["NWSKEY"])
            
        if micro.type == 0:
            endnodes.append(tMicro)
            tMicro.num = 10+i
            i+=1
        else:
            testers.append(tMicro)
            j+=1

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
    
    while True:
        try:
            testnode = next(testnodes)
            assignParams(testnode, {"mode": 0} )
        except:
            break   

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
        print("JOIN Test node " + str(testerThreads.index(x) + 1) )
        x.join(1) 
    
    print("END Test")

def parseTestsToRun(arglist):
    
    
    return ["A1", "A2"]

def main(argv):
    """
    Main program
    
    Read present micros, configure and start the tests as indicated (parameters?)
    
    """ 


    dirTarget = ''
    logName = ''
    try:
        opts, args = getopt.getopt(argv,"hd:l:",["","dir=","log="])
    except getopt.GetoptError:
        print('testMain.py -d <targetdir> -l <logprefix>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('testMain.py -d <targetdir> -l <logprefix>')
            sys.exit()
        elif opt in ("-d", "--dir"):
            dirTarget = arg
        elif opt in ("-l", "--log"):
            logName = arg
    print ('Input file is "', dirTarget)
    print ('Output file is "', logName)

    #List of tests to run, not opt'ed arguments
    testsToRun = parseTestsToRun(args)
           
    configureTestClasses()
    
    for tNo in testsToRun:
        prepareTest(tNo)
    
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

if __name__ == "__main__":
    main(sys.argv[1:])
