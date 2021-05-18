# -----------------------------------------------------------
# Test Executor for the I4S performance test - Test module
#
# Created May, 17, 2021
#
# (C) 2017-2021 Hofer Florian, Bolzano, ITALY
# Released under GNU Public License (GPL)
# email info@florianhofer.it
# -----------------------------------------------------------

# Define enumerations used in class
LORA, LORAWAN, LORAWANTT = 0, 1, 2

class Test():
    '''
    Test main execution module
    '''

    def __init__(self, micro):
        '''
        Constructor
        '''
        self.micro = micro
        self._rstate = 0
        self._mode = LORA
        self._freq = 8683
        self._conf = True
        self._OTAA = False
        self._repc = 5
    
    @property
    def freq(self):
        return self._freq
    
    @freq.setter
    def freq(self, nfrq):
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
    def repeatCount(self, nrpc):
        self._repc = nrpc
                       
    def runTest(self):
        '''
        Start test
        '''
        self.__writeParams()
        try:
            self.micro.write("R\n")
            self._rstate = 1
        except:
            # TODO: manage error 
            pass
        
    def poll(self):        
        '''
        Poll test
        '''
        while self._rstate == 1:
            rbuf = self.micro.read()
            print(rbuf)
            #parse -> output?
        
    def __writeParams(self):
        '''
        Write all test parameters
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

        pars += "m" + self._mode
        if self._mode == 0:
            pars+= "f"+self._freq

        pars += "r"+self._repc
            
        self.micro.write(pars + "\n")
