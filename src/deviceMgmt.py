''' 
-----------------------------------------------------------
Test Executor for the I4S performance testRun - Device module

Created May, 13, 2021
(C) 2017-2021 Hofer Florian, Bolzano, ITALY
Released under GNU Public License (GPL)
email info@florianhofer.it
-----------------------------------------------------------
''' 

import sys
import serial.tools.list_ports

if __name__ == '__main__':
    pass
                
class Micro():
    '''
    Class to store and manage attached devices
    '''
    
    def __init__(self, port):
        '''
        Constructor, initialize variables and I/O
        '''
        self.s = self.openSerial(port)
        self.T = self.detectType()
        self._EUI = self._readEUI()
        
    def openSerial(self, port): 
        try:
            sopen = serial.Serial(port, timeout = 0.1, #Defaults 9600, EIGHTBITS, PARITY_NONE, STOPBITS_ONE)
                              write_timeout = 0.1)  
        except (OSError, serial.SerialException) as e:
            sys.exit("Could not open serial port for interface ({0}:{1}".format(port, str(e)))
        return sopen
            
    def __del__(self):
        '''
        Destructor, reset status
        '''
        self.s.close()
        
    def type(self):
        '''
        Return micro type
        '''
        return self.T

    def detectType(self):
        '''
        Determine the type of the microcontoller, 0 - EN, 1 - TN
        '''
        self.write("T\n")
        try: 
            resp = self.read()
            if resp.startswith("MKRWAN"):
                return 1
            elif resp.startswith("AVR"):
                return 0
            else:
                raise Exception("Unknown micro type")
        except Exception as e:
            print("Could not detect micro interface :{}".format(str(e)))
    
    def _readEUI(self):
        '''
        Determine the EUI of the attached microcontoller
        '''
        self.write("I\n")
        try: 
            resp = self.read()
            if len(resp) == 17:
                self._EUI = resp[:-1]
                return self._EUI
            else:
                raise Exception("EUI read length error")
        except Exception as e:
            print("Could not read micro EUI :{}".format(str(e)))

    @property
    def EUI(self):
        return self._EUI
        
    def read(self, length=255):
        '''
        Read from device, returns string read line by line
        '''
        ret = self.s.read_until(size=length)
        return ''.join([chr(x) for x in ret])
    
    def write(self, msg):
        '''
        Write to device, returns number written
        '''
        return self.s.write(msg.encode())

microList  = []

def findArduinos ():
    '''
    Find Arduino(s) connected to the system, store and add them to List

    :raises EnvironmentError:
        On unsupported or unknown platforms
    :returns:
        A list of the serial ports available on the system
        
    '''
    
    ports = serial.tools.list_ports.comports()
    
    for port, desc, hwid in sorted(ports):
        if "Arduino" in desc or "VID:PID=2341" in hwid:
            microList.append(Micro(port))
            print("->* ", end='')
        else:
            print("    ", end='')

        print("{}: {} [{}]".format(port, desc, hwid))

    return microList
