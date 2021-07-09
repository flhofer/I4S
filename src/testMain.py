''' 
-----------------------------------------------------------
Test Executor for the I4S performance testRun - Main module

Created May, 13, 2021
(C) 2017-2021 Hofer Florian, Bolzano, ITALY
Released under GNU Public License (GPL)
email info@florianhofer.it
-----------------------------------------------------------
''' 

#import project modules
import deviceMgmt, testRun
#import python modules
import sys, getopt, time, threading, os, socket
#import test parameters from parameter module
from testParameters import deviceParameters, testLength, testParameters

#Hardware configurations
endnodes = []
testers = []

commSock = None

'''
Custom exception classes
'''
class NotEnoughMicrosError(Exception):
    """Exception raised for insufficient amount of test devices.

    :attributes
        count   -- number of present micros 
        message -- explanation of the error
    """

    def __init__(self, count, message="Not enough micros available"):
        self.count = count
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.count} -> {self.message}'

def configureTestClasses(logDir="", logPre=""):
    '''
    create and configure testRun devices
    '''
    deviceMgmt.findArduinos()
    
    i=0
    j=0
    #assign to testRun instances
    for micro in deviceMgmt.microList:
        tMicro = testRun.Test(micro, j, logDir, logPre)
        
        if micro.EUI in deviceParameters :
            tMicro.OTAAparams(deviceParameters[micro.EUI]["APPEUI"], deviceParameters[micro.EUI]["APPKEY"])
            tMicro.ABPparams(deviceParameters[micro.EUI]["DEVADDR"], deviceParameters[micro.EUI]["APPSKEY"], deviceParameters[micro.EUI]["NWSKEY"])
            
        if micro.type == 0:
            endnodes.append(tMicro)
            tMicro.num = 10+i
            i+=1
        else:
            testers.append(tMicro)
            j+=1

#TODO function to check for list of parameters, i.e. changes, repeat ecc 

def assignParams(node, params):
    '''
    Assign parameters to micro controller device
    
    :parameter  node: micro controller node to configure
                params: list of parameters to set
            
    :raises    could raise exceptions from called methods (not expected)
    
    '''
    
    node.clearParameters()
    for key in params:
            if type(params[key]) == list:
                param = params[key][0]
            else:
                param = params[key]
            if key == 'mode':
                node.mode = param
            elif key == 'freq': 
                node.frequency = param
            elif key == 'conf': 
                node.confirmed = bool(param)
            elif key == 'OTAA': 
                node.otaa = bool(param) 
            elif key == 'repeat': 
                node.repeatCount = param
            elif key == 'chnMsk': 
                node.channelMask = param
            elif key == 'power': 
                node.powerIndex = param
            elif key == 'dataLen':
                node.dataLength = param
            elif key == 'dataRate': 
                node.dataRate = param
            elif key == 'usePB':
                node.usePB = param

def prepareTest(testNumber, skipNodes=0, skipTest=0):
    '''
    Configure end and testRun nodes with the set parameters
    
    :parameter testNumber to look for in the list of test parameters
    
    :raises    ValueError if test is not defined
               NotEnoughMicrosError if the test defines more micros than available
    
    '''

    try: 
        params = [x for x in testParameters if x["testRun"] == testNumber][0]    
        print ("Parameters for test:", params)
    except IndexError as e:
        raise ValueError("Parameters for '{}' not found".format(testNumber)) from e
     
    nodes = iter(endnodes)
    for nodeParams in params["NodeParam"]:
        if skipNodes > 0:
            skipNodes -= 1
        else:
            try:
                endnode = next(nodes)
            except StopIteration:
                raise NotEnoughMicrosError (endnodes.count)
        
            assignParams(endnode, nodeParams)                        
  
    while True:
        try:
            endnode = next(nodes)
            assignParams(endnode, {"mode": 0} )
        except StopIteration:
            break
        except: # forward all other exceptions, Explicit!
            raise 
          
    testnodes = iter(testers)
    for testParms in params["TestParam"]:
        if skipTest > 0:
            skipTest -= 1
        else:
            try:
                testnode = next(testnodes)
            except StopIteration:
                raise NotEnoughMicrosError (testers.count)
            
            assignParams(testnode, testParms)
    
    while True:
        try:
            testnode = next(testnodes)
            assignParams(testnode, {"mode": 0} )
        except StopIteration:
            break
        except: # forward all other exceptions, Explicit!
            raise 

testerThreads = []
            
def runTest():
    '''
    Sequentially start and run test and end nodes
    
    Loops are executed in separate threads
    
    '''
    
    testerThreads.clear()
    print("START Test")
    for testNode in testers:
        print("RUN Test node " + str(testers.index(testNode) + 1) )
        testNode.runTest()
        

    for testNode in testers:
        print("Threading Test node " + str(testers.index(testNode) + 1) )
        x = threading.Thread(target=testNode.poll, args = ())
        x.start()
        testerThreads.append(x)
   
    time.sleep(1) 
    for endnode in endnodes:
        print("RUN End node " + str(endnodes.index(endnode) + 1) )
        endnode.runTest()
        endnode.poll()

def stopTest():
    '''
    Stop previously started tests
    '''
    
    for testNode in testers:
        print("STOP Test node " + str(testers.index(testNode) + 1) )
        testNode.stopTest()

    time.sleep(1) 
        
    for x in testerThreads :
        print("JOIN Test node " + str(testerThreads.index(x) + 1) )
        x.join(1) 
    
    print("END Test")    

def parseTestsToRun(argList):
    '''
    Parse command line arguments to create list of tests to execute
    
    :parameter    argList contains a list of strings to parse with wildcards ecc
    
    :returns      a sorted list of strings containing each test's ID
    
    '''
    if argList == []:
        argList = ["**"]

    testList = []
    for arg in argList:
        if len(arg) > 2:
            raise ValueError("Invalid test parameter, '{}'".format(arg))
        if arg[1] == '*':
            if arg[0] == '*':
                for grp in testLength:
                    for no in range(1, testLength[grp] + 1):
                        testList.append( grp + str(no))
            else:        
                for no in range(1, testLength[arg[0]] + 1):
                            testList.append(arg[0] + str(no))
        elif arg[0] == '*':
            for grp in testLength:
                testList.append(grp + arg[1])
            
        else:
            if testLength[arg[0]] < int(arg[1]):
                raise LookupError("Test parameter index out of bounds, '{}'".format(arg))
                
            testList.append(arg)
                
    return sorted(testList)

def syncSetup(mode):
    
    port = 3212
    global commSock
    if mode == 1: 
        print("Establishing connection..")
        while True:                
            try:
                commSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host = socket.gethostbyname("")
                commSock.connect((host, port))
                break
            except ConnectionRefusedError:
                time.sleep(1)
            
    else:
        commSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostbyname("")  # get local machine name
        commSock.bind((host, port))
        print("Waiting for incoming..")
        commSock.listen(1)          # accept only one connection
        commSock, addr = commSock.accept() # replace with listener
        print("Connection from: " + str(addr))

def syncComm(mode):
    if mode == 0:
        return
    global commSock
    if mode == 1:
        data = ""
        while data != "s":
            commSock.send("S".encode('utf-8'))
            data = commSock.recv(128).decode('utf-8')
    else:
        while True:
            data = commSock.recv(128).decode('utf-8')
            if data == "S":
                commSock.send("s".encode('utf-8'))
                break

def main(argv):
    """
    Main program
    
    Read present micros, configure and start the tests as indicated (parameters?)
    
    :parameter    argv arguments list passed to main command 
    
    """
     
    dirTarget = ''
    logName = ''
    skipNodes = 0
    skipTest = 0
    sync = 0
    try:
        opts, args = getopt.getopt(argv,"hd:e:l:Sst:",["dir=","log="])
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
        elif opt in ("-e"):
            skipNodes = int(arg)
        elif opt in ("-t"):
            skipTest = int(arg)
        elif opt in ("-S"): # server - slave
            sync = 2
            syncSetup(2)
        elif opt in ("-s"): # client - master
            sync = 1
            syncSetup(1)
    print ('Log directory is "', dirTarget)
    print ('Base log name "', logName)

    if not os.path.isdir(dirTarget):
        dirTarget = ''

    #List of tests to run, not opt'ed arguments
    testsToRun = parseTestsToRun(args)
           
    configureTestClasses(dirTarget, logName)
    
    for tNo in testsToRun:
        prepareTest(tNo, skipNodes, skipTest)
    
        syncComm(sync)        
        runTest()
        syncComm(sync)        
        stopTest()
        syncComm(sync)
        
    if commSock:
        commSock.close()
   
    # Trigger destructor call
    del deviceMgmt.microList

if __name__ == "__main__":
    main(sys.argv[1:])
