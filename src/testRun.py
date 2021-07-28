''' 
-----------------------------------------------------------
Test Executor for the I4S performance testRun - Test module

Created May, 17, 2021
(C) 2017-2021 Hofer Florian, Bolzano, ITALY
Released under GNU Public License (GPL)
email info@florianhofer.it
-----------------------------------------------------------
''' 

import time, sys

# Define enumerations used in class
DISABLED, OFF, LORA, LORAWAN, LORAWANRT, LORAJOIN = -1, 0, 1, 2, 3, 4

class Test():
    '''
    Test main execution module
    '''

    def __init__(self, micro, num=1, logDir="", logPre=""):
        '''
        Constructor and initialize default value
        '''
        self._micro = micro
        self._logFile = None
        self._logDir = logDir
        self._logPre = logPre
        self._num = num
        
        '''
        Runtime parameters, connection LoRa
        '''
        self._AEui  = ""
        self._AKey  = ""
        self._DAdr  = ""
        self._ASKey = ""
        self._NSKey = ""
        
        self.clearParameters()

    def clearParameters(self):
        '''
        Clear and reset to default the runtime parameters
        '''
        
        self._rstate = 0
        self._mode = LORA
        self._freq = 8683
        self._conf = False
        self._OTAA = False
        self._repc = 1
        self._chMsk = 0xff
        self._power = 1 # ETSI 14dBm default
        self._dlen = 16
        self._drate = 255
        self._usePB = True
        self._writeLog = False
        self._BW = 125
        self._SF = 12
        self._CR = 8
        
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
        if self._rstate > 0:
            raise Exception("Can not change value while running!!")        
        self._mode = nMode

    @property
    def frequency(self):
        return self._freq
    
    @frequency.setter
    def frequency(self, nfrq):
        if self._mode != 1:
            raise Exception("Incorrect device mode for this setting!!")
        self._freq = nfrq
        
    @property
    def confirmed(self):
        return self._conf
    
    @confirmed.setter
    def confirmed(self, ncnf):
        if self._mode < 2:
            raise Exception("Incorrect device mode for this setting!!")
        self._conf = ncnf
        
    @property
    def otaa(self):
        return self._OTAA
    
    @otaa.setter
    def otaa(self, notaa):
        if self._mode < 2:
            raise Exception("Incorrect device mode for this setting!!")
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
        if self._mode < 2:
            raise Exception("Incorrect device mode for this setting!!")
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
        if self._mode < 2:
            raise Exception("Incorrect device mode for this setting!!")
        self._drate = nDR
    
    def ABPparams(self, DAdr, ASKey, NSKey):
        self._DAdr  = DAdr
        self._ASKey = ASKey
        self._NSKey = NSKey
        self._OTAA = False

    def OTAAparams(self, AEui, AKey):
        self._AEui  = AEui
        self._AKey = AKey
        self._OTAA = True
    
    @property
    def logFile(self):
        return self._logFile

    @property
    def num(self):
        return self._num
    
    @num.setter
    def num(self, nnum):
        if self._rstate > 0:
            raise Exception("Can not change value while running!!")
        self._num = nnum
 
    @property
    def usePB(self):
        return self._usePB
    
    @usePB.setter
    def usePB(self, use):
        if self._mode < 2:
            raise Exception("Incorrect device mode for this setting!!")
        self._usePB = use   

    @property
    def SF(self):
        return self._SF

    @SF.setter
    def SF(self, newSF):
        if self._mode != 1:
            raise Exception("Incorrect device mode for this setting!!")
        self._SF = newSF  
    
    @property
    def CR(self):
        return self._CR

    @CR.setter
    def CR(self, newCR):
        if self._mode != 1:
            raise Exception("Incorrect device mode for this setting!!")
        self._CR = newCR  

    @property
    def BW(self):
        return self._BW

    @BW.setter
    def BW(self, newBW):
        if self._mode != 1:
            raise Exception("Incorrect device mode for this setting!!")
        self._BW = newBW  
                                                    
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
                path = ''
                if self._logDir != '':
                    path += self._logDir + '/'
                if self._logPre != '':
                    path += self._logPre
                else:
                    path += time.strftime("%Y%m%d-%H%M%S") 
                path += "-tdev{0:02d}".format(self._num) + ".log"
                self._logFile = open (path, "a")
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
            print("Parameter writing exception, {}".format(e))
            self._mode = DISABLED
        
    def poll(self):        
        '''
        Poll test, has to be run as thread!
        '''
        rbuf = " " 
        while (rbuf != "") or (self._rstate == 1):

            rbuf = self._micro.read()
            while rbuf != "":
                self.__parseBuffer(rbuf[:-1])
                self._logFile.write(rbuf)
                rbuf = self._micro.read()

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
        
        pars += "m" + str(self._mode)
        if self._mode == 1:
            pars+= "f" + str(self._freq)
            pars+= "b" + str(self._BW)
            pars+= "s" + str(self._SF)
            pars+= "c" + str(self._CR)
        elif self._mode > 1:
            if self.otaa:
                pars += "o"
            else:
                pars += "a"
                
            if self._conf:
                pars += "c"
            else:
                pars += "u"

            pars += "r" + str(self._repc)
            pars += "C" + "%0.2Xh" % self._chMsk
            pars += "p" + str(self._power)
            pars += "d" + str(self._drate) 
        pars += "l" + str(self._dlen)
        # pars += "n"
        
        self.__writeMicro(pars)
        
        if self._mode > 1:
            if self._usePB:
                if self._OTAA == True:
                    self.__writeMicro("E" + self._AEui.upper() + "h")
                    self.__writeMicro("K" + self._AKey.upper() + "h")
                else:
                    self.__writeMicro("D" + self._DAdr.upper() + "h")
                    self.__writeMicro("N" + self._NSKey.upper()+ "h")
                    self.__writeMicro("A" + self._ASKey.upper()+ "h")
            else:
                if self._OTAA == True:
                    self.__writeMicro("E01234567890abcdef01234567890abcdh")
                    self.__writeMicro("K01234567890abcdef01234567890abcdh")
                else:
                    self.__writeMicro("D01234567h")
                    self.__writeMicro("N01234567890abcdef01234567890abcdh")
                    self.__writeMicro("A01234567890abcdef01234567890abcdh")               

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
            raise Exception("Unable to set parameter on Micro {1}, it responds '{0}'".format(response[:-1], parms))

    def __parseBuffer(self, buf):
        if buf.startswith("Results"):
            self._writeLog = True 
        
        if self._micro.T == 0: 
            print(buf, file=sys.stderr)
            if self._writeLog == True:
                print(buf) # print results to stdout

        if buf.startswith("done"):
            self._rstate = 0
            self._writeLog = False
            