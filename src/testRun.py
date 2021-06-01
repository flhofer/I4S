''' 
-----------------------------------------------------------
Test Executor for the I4S performance testRun - Test module

Created May, 17, 2021
(C) 2017-2021 Hofer Florian, Bolzano, ITALY
Released under GNU Public License (GPL)
email info@florianhofer.it
-----------------------------------------------------------
''' 

import time

# Define enumerations used in class
DISABLED, LORA, LORAWAN, LORAWANTT = -1, 0, 1, 2

class Test():
    '''
    Test main execution module
    '''

    def __init__(self, micro):
        '''
        Constructor and initialize default value
        '''
        self._micro = micro
        self._rstate = 0
        self._mode = LORA
        self._freq = 8683
        self._conf = True
        self._OTAA = False
        self._repc = 5
        self._chMsk = 0xff
        self._power = 0
        self._dlen = 1
        self._drate = 5
    
        '''
        Runtime parameters, connection LoRa
        '''
        self._updateL = False   # update LoRaWan parameters
        self._AEui  = ""
        self._AKey  = ""
        self._DAdr  = ""
        self._ASKey = ""
        self._NSKey = ""
        
        self._logFile = None
    
    def __del__(self):
        '''
        Destructor, close and clear
        '''
        if self._logFile:
            self._logFile.close()
   
    '''
    Getters and setters
    '''
    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def mode(self, nMode):
        self._mode = nMode

    @property
    def frequency(self):
        return self._freq
    
    @frequency.setter
    def frequency(self, nfrq):
        self._freq = nfrq
        
    @property
    def confirmed(self):
        return self._conf
    
    @confirmed.setter
    def confirmed(self, ncnf):
        self._conf = ncnf
        
    @property
    def otaa(self):
        return self._OTAA
    
    @otaa.setter
    def otaa(self, notaa):
        self._OTAA = notaa

    @property
    def repeatCount(self):
        return self._repc
    
    @repeatCount.setter
    def repeatCount(self, nMsk):
        self._repc = nMsk

    @property
    def channelMask(self):
        return self._chMsk
    
    @channelMask.setter
    def channelMask(self, nrpc):
        self._chMsk = nrpc

    @property
    def powerIndex(self):
        return self._power
    
    @powerIndex.setter
    def powerIndex(self, nPwr):
        self._power = nPwr

    @property
    def dataLength(self):
        return self._dlen
    
    @dataLength.setter
    def dataLength(self, nDlen):
        self._dlen = nDlen

    @property
    def dataRate(self):
        return self._drate
    
    @dataRate.setter
    def dataRate(self, nDR):
        self._drate = nDR
    
    def ABPparams(self, DAdr, ASKey, NSKey):
        self._DAdr  = DAdr
        self._ASKey = ASKey
        self._NSKey = NSKey
        self._OTAA = False
        self._updateL = True

    def OTAAparams(self, AEui, AKey):
        self._AEui  = AEui
        self._AKey = AKey
        self._OTAA = True
        self._updateL = True
    
    @property
    def logFile(self):
        return self._logFile
                    
    '''
    Test execution methods
    '''                                           
    def runTest(self):
        '''
        Start test
        
        :raises Exception:
            When configuration writing is not possible
        :returns:
            
        '''
        if self._mode == DISABLED:
            print("Disabled")
            raise Exception("Disabled")
            
        self.configureTest()
        
        ''' Check again after configuration '''
        if self._mode == DISABLED:
            print("Disabled")
            raise Exception("Disabled")
        
        try:
            self._micro.write("R\n")
            self._rstate = 1            
        except Exception as e:
            raise Exception ("Unable to write start command {}".format(str(e))) 
        finally:
            try:
                if self._logFile:
                    self._logFile.close()
                self._logFile = open (time.strftime("%Y%m%d-%H%M%S") + ".log", "w")
            except Exception as e:
                raise Exception ("Unable to create log-file {}".format(str(e))) 

    def configureTest(self):
        '''
        Configure test

        :raises Exception:
            When configuration writing is not possible
        :returns:

        '''
        try:
            self.__writeParams()
        except Exception as e:
            print("Parameter writing exception, {}", e)
            self._mode = DISABLED
        
    def poll(self):        
        '''
        Poll test, has to be run as thread!
        '''
        while self._rstate == 1:
            rbuf = self._micro.read()
            if rbuf != "" :
                print(rbuf)
                self.__parseBuffer(rbuf[:-1])
                self._logFile.write(rbuf)
                
            time.sleep(0.1)
    
    def stopTest(self):
        try:
            self._micro.write("S\n")
        except Exception as e:
            raise Exception ("Unable to write stop command {}".format(str(e)))       

    def stopPoll(self):
        self._rstate = 0
        
    def __writeParams(self):
        '''
        Write all test parameters

        :raises Exception:
            When configuration writing is not possible
        :returns:
        
        '''
        pars = ""

        if self.otaa:
            pars += "o"
        else:
            pars += "a"
        
        if self._conf:
            pars += "c"
        else:
            pars += "u"

        pars += "m" + str(self._mode)
        if self._mode == 0:
            pars+= "f" + str(self._freq)

        pars += "r" + str(self._repc)
        pars += "C" + "%0.2Xh" % self._chMsk
        pars += "p" + str(self._power)
        pars += "l" + str(self._dlen)
        pars += "d" + str(self._drate) 
        # pars += "n"
        
        print ("Parameter write: '{}'".format(pars))
        self.__writeMicro(pars)
        
        if self._updateL == True:
            if self._OTAA == True:
                self.__writeMicro("E" + self._AEui.upper() + "h")
                self.__writeMicro("K" + self._AKey.upper() + "h")
            else:
                self.__writeMicro("D" + self._DAdr.upper() + "h")
                self.__writeMicro("N" + self._NSKey.upper()+ "h")
                self.__writeMicro("A" + self._ASKey.upper()+ "h")

    def __writeMicro(self, parms):
        '''
        Write line to Micro and check for responses

        :raises Exception:
            When configuration writing is not possible
        :returns:

        '''
        self._micro.write(parms + "\n")
        response = self._micro.read()
        if response != "":
            raise Exception("Unable to set parameter on Micro, it responds '{0}'".format(response[:-1]))

    def __parseBuffer(self, buf):
        if buf.startswith("done"):
            self._rstate = 0
            