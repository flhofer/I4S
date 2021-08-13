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
import sys, getopt, time, threading, os, socket, ipaddress, itertools
#import test parameters from parameter module
from testParameters import testLength, testParameters, nodeDlen, maxDataLen
from deviceParameters import deviceParameters

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

def configureTestClasses(logDir="", logPre="", skipNodes=0, skipTest=0):
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
            tMicro.num = 10+i+skipNodes
            i+=1
        else:
            testers.append(tMicro)
            tMicro.num = j+skipTest
            j+=1

#TODO function to check for list of parameters, i.e. changes, repeat ecc 

def setParam(node, key, param):
    '''
    Set a parameter parameters of the micro
        
    :parameter  node: micro controller node to configure
                key: key to set
                param: list of parameters to set
            
    :raises    could raise exceptions from called methods (not expected)
    
    '''
        
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
    elif key == 'bandWidth':
        node.BW = param
    elif key == 'codeRate':
        node.CR = param
    elif key == 'spreadFactor':
        node.SF = param
    elif key == 'usePB':
        node.usePB = param
    elif key == 'rx1Delay':
        node.rx1Delay = param
    elif key == 'noReset':
        node.noReset = bool(param)
    elif key == 'noDCycle':
        node.noDCycle = bool(param)
    elif key == 'private':
        node.private = bool(param)
    elif key == 'xHeader':
        node.xHeader = bool(param)
    elif key == 'invertQ':
        node.invertQ = bool(param)
    elif key == 'useCRC':
        node.useCRC = bool(param)
    elif key == 'simLWan':
        node.simLWan = bool(param)
    elif key == 'preamble':
        node.preLen = param
    elif key == 'limit':
        pass
    else: 
        raise Exception("Unknown parameter '{}:{}'".format(key, param))

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
        
        setParam(node, key, param)


#TODO: experimental, not working yet
def generateVarParam(params):
    nodeList = []
    for key in params:
        if type(params[key]) == list:
            for param in params[key]:
                nodeList.append({key : param})
    
    return nodeList

def generateParams(testParam):
    '''
    Generate a list of parameters to vary during test execution
    
    :parameter  node: micro controller node to configure
                params: list of parameters to set
            
    :raises    could raise exceptions from called methods (not expected)
    
    '''

    tests = []
    for params in testParam["NodeParam"]:
        nodeT = generateVarParam(params)
        if nodeT != []:
            tests.append(nodeT)

    for params in testParam["TestParam"]:
        nodeT = generateVarParam(params)
        if nodeT != []:
            tests.append(nodeT)
            
    # a = [[1,2,3],[4,5,6],[7,8,9,10]]
    return list(itertools.product(*tests))
            
def prepareTest(testNumber, sync=0, skipNodes=0, skipTest=0, dlen=0):
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
                if sync != 1:
                    raise NotEnoughMicrosError (endnodes.count)
                else:
                    break
        
            assignParams(endnode, nodeParams)   # all parameters
            if not "limit" in nodeParams or nodeParams["limit"]!= 0:
                if  (endnode.dataRate == 255):
                    dlen = min(int(maxDataLen[0]), dlen)
                else:
                    dlen = min(int(maxDataLen[endnode.dataRate]), dlen)
            if not "noStop" in nodeParams or nodeParams["noStop"]!= 1:
                setParam(endnode, "dataLen", dlen)  # data length for this test
                endnode.noStop = False
            else:
                # ignore dataLen from test, use parameter
                endnode.noStop = True

            endnode.poll()
  
    while True:
        try:
            endnode = next(nodes)
            assignParams(endnode, {"mode": 0} )
            endnode.noStop = False
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
                if sync != 1:
                    raise NotEnoughMicrosError (testers.count)
                else:
                    break
            
            assignParams(testnode, testParms)
            testnode.poll()
    
    while True:
        try:
            testnode = next(testnodes)
            assignParams(testnode, {"mode": 0} )
        except StopIteration:
            break
        except: # forward all other exceptions, Explicit!
            raise 

testerThreads = []
endnodeThreads = []
            
def runTest():
    '''
    Sequentially start and run test and end nodes
    
    Loops are executed in separate threads
    
    '''
    
    testerThreads.clear()
    endnodeThreads.clear()
    print("START Test")
    for testNode in testers:
        print("RUN Test node " + str(testers.index(testNode) + 1) )
        testNode.runTest()
        

    for testNode in testers:
        print("Threading Test node " + str(testers.index(testNode) + 1) )
        x = threading.Thread(target=testNode.poll, args = ())
        x.start()
        testerThreads.append(x)
   
    time.sleep(5)
    ran = 0 
    for endnode in endnodes:
        if endnode.mode == 0:
            pass
        else:            
            print("RUN End node " + str(endnodes.index(endnode) + 1) )
            endnode.runTest()
            if endnode.noStop == True:
                x = threading.Thread(target=endnode.poll, args = ())
                x.start()
                endnodeThreads.append(x)
            else: 
                ran = 1
                endnode.poll()

    return ran

def stopTest():
    '''
    Stop previously started tests
    '''
    
    for testNode in testers:
        print("STOP Test node " + str(testers.index(testNode) + 1) )
        testNode.stopTest()

    for endnode in endnodes:
        if endnode.mode != 0 and endnode.noStop == True:
            print("STOP End node " + str(endnodes.index(endnode) + 1) )
            endnode.stopTest()
        else:            
            pass

    time.sleep(1) 
        
    for x in testerThreads :
        print("JOIN Test node " + str(testerThreads.index(x) + 1) )
        x.join(1) 

    for x in endnodeThreads :
        print("JOIN End node " + str(endnodeThreads.index(x) + 1) )
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

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def syncSetup(mode, host):
    
    port = 3212
    global commSock
    if mode == 1: 
        while True:                
            try:
                commSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print("Establishing connection..", host)
                commSock.connect((host, port))
                break
            except ConnectionRefusedError:
                time.sleep(1)
            
    else:
        commSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Waiting for incoming..", host)
        commSock.bind((host, port))
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
            data = commSock.recv(1024).decode('utf-8')
            if data.startswith("ERROR"):
                print(data)
    else:
        while True:
            data = commSock.recv(1024).decode('utf-8')
            if data == "S":
                commSock.send("s".encode('utf-8'))
                break

def sendToClient(string):
    global commSock
    commSock.send(("ERROR from slave: " + string).encode('utf-8'))

def main(argv):
    """
    Main program
    
    Read present micros, configure and start the tests as indicated (parameters?)
    
    :parameter    argv arguments list passed to main command 
    
    """
     
    dirTarget = '/tmp'
    logName = 'test'
    skipNodes = 0
    skipTest = 0
    sync = 0
    useIp = ""
    firstOnly = False

    try:
        opts, args = getopt.getopt(argv,"hd:e:fi:l:Sst:",["dir=","log="])
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
        elif opt in ("-f"):
            firstOnly = True
        elif opt in ("-t"):
            skipTest = int(arg)
        elif opt in ("-S"): # server - slave
            sync = 2
            if useIp == "":
                useIp = get_ip() # get local machine name
        elif opt in ("-s"): # client - master
            sync = 1
            if useIp == "":
                useIp = str(ipaddress.ip_address(get_ip())+1) # By default we match IP addresses next to each other
        elif opt in ("-i"):
            useIp = arg
    print ('Log directory is "{}"'.format(dirTarget))
    print ('Base log name "{}"'.format(logName))

    if sync != 0:
        syncSetup(sync, useIp)

    if not os.path.isdir(dirTarget):
        dirTarget = ''

    #List of tests to run, not opt'ed arguments
    testsToRun = parseTestsToRun(args)
           
    configureTestClasses(dirTarget, logName, skipNodes, skipTest)
    
    for tNo in testsToRun:
        for dlen in nodeDlen:
            print('Test/Datalen: ', tNo, dlen)
            try:
                prepareTest(tNo, sync, skipNodes, skipTest, dlen)
        
                syncComm(sync)        
                if runTest() == 0 and sync == 0:
                    input('Press enter to stop...')
                syncComm(sync)        
                stopTest()
                syncComm(sync)
            except Exception as e:
                if sync == 2:
                    sendToClient(str(e))
                raise
            
            if firstOnly == True:
                break
        
    if commSock:
        commSock.close()
   
    # Trigger destructor call
    del deviceMgmt.microList

if __name__ == "__main__":
    main(sys.argv[1:])
