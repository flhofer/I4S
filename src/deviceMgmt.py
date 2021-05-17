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
import sys

if __name__ == '__main__':
    pass

class ReadLine:
    def __init__(self, s):
        self.buf = bytearray()
        self.s = s
    
    def readline(self):
        i = self.buf.find(b"\n")
        if i >= 0:
            r = self.buf[:i+1]
            self.buf = self.buf[i+1:]
            return r
        while True:
            i = max(1, min(2048, self.s.in_waiting))
            data = self.s.read(i)
            i = data.find(b"\n")
            if i >= 0:
                r = self.buf + data[:i+1]
                self.buf[0:] = data[i+1:]
                return r
            else:
                self.buf.extend(data)
                
class Micro:
    def read(self, length=255, timeout=100):
        """Read from device, returns string read"""
        print("Not implemented")
        return ""
            
    def write(self, msg, timeout=100):
        """Write to device, returns number written"""
        print("Not implemented")
        return 0

class MicroUSB(Micro):
    """Class to store and manage attached devices"""
    
    def __init__(self, device):
        """Constructor, initialize variables and I/O"""
        self.device = device
        self.def_intf = 1
        self.reattach = False
        stx = '%04x %04x: '+str(self.device._manufacturer).strip()+' = '+str(self.device._product).strip()
        print (stx % (self.device.idVendor,self.device.idProduct))
        self.__getEndPoints()
        
    def __del__(self):
        """Destructor, reset status"""
        if self.reattach:
            try:
                usb.util.dispose_resources(self.device)
                self.device.attach_kernel_driver(0)
            except usb.core.USBError as e:
                sys.exit("Could not re-attatch kernel driver from interface({0}:{1}".format(self.def_intf, str(e)))

    def __getEndPoints(self):
        """Set configuration and retrieve Endpoints for interfaces"""

        #  check if kernel driver is loaded, detach in case
        if self.device.is_kernel_driver_active(self.def_intf):
            try:
                self.device.detach_kernel_driver(self.def_intf)
                self.reattach = True
            except usb.core.USBError as e:
                sys.exit("Could not detatch kernel driver from interface({0}:{1}".format(self.def_intf, str(e)))

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
        """Read from device, returns string read"""
        ret = self.portR.read(length, timeout)
        return ''.join([chr(x) for x in ret])
        # assert len(sret) == length
        # return ret
        # sret = ''.join([chr(x) for x in ret])
        # assert sret == msg
    
    def write(self, msg, timeout=100):
        """Write to device, returns number written"""
        return self.portW.write(msg, timeout)

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
                microList.append(MicroUSB(micro))
            except:
                traceback.print_exc()
