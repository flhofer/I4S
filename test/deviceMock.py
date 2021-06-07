''' 
-----------------------------------------------------------
Test Executor for the I4S performance testRun - Device mock

Created May, 31, 2021
(C) 2017-2021 Hofer Florian, Bolzano, ITALY
Released under GNU Public License (GPL)
email info@florianhofer.it
-----------------------------------------------------------
''' 

import deviceMgmt

class MicroMock(deviceMgmt.Micro):
    '''
    Mocking class faking to be a micro controller
    '''
    
    def read(self, length=255):
        '''
        Read from device, returns string read line by line
        '''
        try: 
            return self.s.readline(length)
        except:
            print ("MOCK: unable to read from mock file")
            return ""
    
    def write(self, msg):
        '''
        Write to device, returns number written
        '''        
        if "R" in msg:
            self.run = True
        
        self._msgBuff.append(msg)
        return len(msg)

    def clearBuffer(self):
        self._msgBuff = []

    def __init__(self, mType, iofile):
        '''
        Constructor
        '''
        self.T = mType
        self.run = False
        try : 
            self.s = open ( iofile, "r")
        except OSError as e: 
            raise Exception ("Unable to create mock! {}".format(str(e)))
        
        self._EUI = "0123456789ABCDEF"
        self.clearBuffer()    
        
    @property
    def EUI(self):
        return self._EUI
    
    @property
    def buffer(self):
        return self._msgBuff