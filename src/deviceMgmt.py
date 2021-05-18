# -----------------------------------------------------------
# Test Executor for the I4S performance test - Device module
#
# Created May, 13, 2021
#
# (C) 2017-2021 Hofer Florian, Bolzano, ITALY
# Released under GNU Public License (GPL)
# email info@florianhofer.it
# -----------------------------------------------------------

import sys
import serial
import glob

if __name__ == '__main__':
    pass
                
class Micro():
    """Class to store and manage attached devices"""
    
    def __init__(self, port):
        """Constructor, initialize variables and I/O"""
        self.s = self.openSerial(port)
        self.T = self.detectType()
        
    def openSerial(self, port): 
        try:
            sopen = serial.Serial(port, timeout = 0.1, #Defaults 9600, EIGHTBITS, PARITY_NONE, STOPBITS_ONE)
                              write_timeout = 0.1)  
        except (OSError, serial.SerialException) as e:
            sys.exit("Could not open serial port for interface ({0}:{1}".format(port, str(e)))
        return sopen
            
    def __del__(self):
        """Destructor, reset status"""
        self.s.close()
        
    def type(self):
        """Return micro type"""
        return self.T

    def detectType(self):
        """Determine the type of the microcontoller, 0 - EN, 1 - TN"""
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
            
        
    def read(self, length=255):
        """Read from device, returns string read line by line"""
        ret = self.s.read_until(size=length)
        return ''.join([chr(x) for x in ret])
    
    def write(self, msg):
        """Write to device, returns number written"""
        return self.s.write(msg.encode())

microList  = []

def findArduinos ():
    """ Find Arduino(s) connected to the system, store and add them to List

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
        @tfeldmann, option 1, but not possible to filter ACM.s
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            microList.append(Micro(port))
        except (OSError, serial.SerialException):
            pass
    
    # import serial.tools.list_ports
    # ports = serial.tools.list_ports.comports()
    #
    # for port, desc, hwid in sorted(ports):
    #     print("{}: {} [{}]".format(port, desc, hwid))
        # if "Arduino" in p.description:
        # print "This is an Arduino!"
        #

    return microList
