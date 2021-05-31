'''
Created on 31 May 2021

@author: florianhofer
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
        
        if self.run :
            try: 
                return self.iofile.readline()
            except:
                print ("MOCK: unable to read from mock file")
                return ""
    
    def write(self, msg):
        '''
        Write to device, returns number written
        '''
        print ("MOCK: ", msg)
        
        if msg.contains("R"):
            self.run = True
        
        return len(msg)

    def __init__(self, mType, iofile):
        '''
        Constructor
        '''
        self.T = mType
        try : 
            self.iofile = open ( iofile, "r")
        except: 
            print("Unable to create mock!")
    