# -----------------------------------------------------------
# Test Executor for the I4S performance test - Device module
#
# Created May, 13, 2021
#
# (C) 2017-2021 Hofer Florian, Bolzano, ITALY
# Released under GNU Public License (GPL)
# email info@florianhofer.it
# -----------------------------------------------------------

import usb.core
import traceback

if __name__ == '__main__':
    pass

class Micro:
    """Class to store and manage attached devices"""
    def __init__(self, device):
        self.device = device
        self.portW = 0x01 # default entry point
        self.portR = 0x83
        stx = '%04x %04x: '+str(self.device._manufacturer).strip()+' = '+str(self.device._product).strip()
        print (stx % (self.device.idVendor,self.device.idProduct))
        # self.__getPorts()

    def __getPorts(self):
        # for attrib in dir(self.device):
        #     if not attrib.startswith('_') and not attrib == 'configurations':
        #         x=getattr(self.device, attrib)
        #         print ("  ", attrib, x)
        for config in self.device.configurations:
            for attrib in dir(config):
                if not attrib.startswith('_'):
                    x=getattr(config, attrib)
                    print ("    ", attrib, x)
        
    def read(self, length, timeout=100):
        """Read from device"""
        ret = self.device.read(0x81, length, timeout)
        sret = ''.join([chr(x) for x in ret])
        assert len(sret) == length
        return ret
        # sret = ''.join([chr(x) for x in ret])
        # assert sret == msg
    
    def write(self, msg, timeout=100):
        """Write to device"""
        assert len(self.device.write(self.portW, msg, timeout)) == len(msg)

microList = []

def findArduinos ():
    """ Find Arduino(s) connected to the system, store and add them to List """
    
    micros = usb.core.find(find_all=True, idVendor=0x2341)
    for micro in micros:
        if micro != None:
            try:
                if micro._manufacturer is None:
                    micro._manufacturer = usb.util.get_string(micro, micro.iManufacturer)
                if micro._product is None:
                    micro._product = usb.util.get_string(micro, micro.iProduct)
                microList.append(Micro(micro))
            except:
                traceback.print_exc()
                
            

