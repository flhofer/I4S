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
        stx = '%04x %04x: '+str(self.device._manufacturer).strip()+' = '+str(self.device._product).strip()
        print (stx % (self.device.idVendor,self.device.idProduct))
        self.__getEndPoints()

    def __getEndPoints(self):
        """Set configuration and retrieve Endpoints for interfaces"""
        self.device.set_configuration()

        # get an EndPoint instance
        cfg = self.device.get_active_configuration()
        intf = cfg[(1,0)]
        
        self.portW = usb.util.find_descriptor(
            intf,
            # match the first OUT endpoint
            custom_match = \
            lambda e: \
                usb.util.endpoint_direction(e.bEndpointAddress) == \
                usb.util.ENDPOINT_OUT)

        self.portR = usb.util.find_descriptor(
            intf,
            # match the first IN endpoint
            custom_match = \
            lambda e: \
                usb.util.endpoint_direction(e.bEndpointAddress) == \
                usb.util.ENDPOINT_IN)
        
    def read(self, length=255, timeout=100):
        """Read from device"""
        ret = self.portR.read(length, timeout)
        return ''.join([chr(x) for x in ret])
        # assert len(sret) == length
        # return ret
        # sret = ''.join([chr(x) for x in ret])
        # assert sret == msg
    
    def write(self, msg, timeout=100):
        """Write to device"""
        # assert len(
        self.portW.write(msg, timeout)
            # ) == len(msg)

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

        
        

