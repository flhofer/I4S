# -----------------------------------------------------------
# Test Executor for the I4S performance testRun - Device mock
#
# Created May, 31, 2021
#
# (C) 2017-2021 Hofer Florian, Bolzano, ITALY
# Released under GNU Public License (GPL)
# email info@florianhofer.it
# -----------------------------------------------------------

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
            return self.s.readline()
        except:
            print ("MOCK: unable to read from mock file")
            return ""
    
    def write(self, msg):
        '''
        Write to device, returns number written
        '''
        print ("MOCK: ", msg)
        
        if "R" in msg:
            self.run = True
        
        return len(msg)

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
    