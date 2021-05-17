# -----------------------------------------------------------
# Test Executor for the I4S performance test - Test module
#
# Created May, 17, 2021
#
# (C) 2017-2021 Hofer Florian, Bolzano, ITALY
# Released under GNU Public License (GPL)
# email info@florianhofer.it
# -----------------------------------------------------------
import deviceMgmt

class Test():
    '''
    Test main execution module
    '''

    def __init__(self, micro):
        '''
        Constructor
        '''
        self.micro = micro
        self.rstate = 0
        
    def runTest(self):
        '''
        Start test
        '''
        self.__writeParams()
        try:
            self.micro.write("R\n")
            self.rstate = 1
        except:
            # TODO: manage error 
            pass
        
    def poll(self):        
        '''
        Poll test
        '''
        while self.rstate == 1:
            rbuf = deviceMgmt.microList[0].readline()
            print(rbuf)
            #parse -> output?
        
    def __writeParams(self):
        '''
        Write all test parameters
        '''
        with self.micro as deviceMgmt.Micro:
            
        