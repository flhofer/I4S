''' 
-----------------------------------------------------------
Unit Test for the I4S performance testRun - Test Run

Created May, 31, 2021
(C) 2017-2021 Hofer Florian, Bolzano, ITALY
Released under GNU Public License (GPL)
email info@florianhofer.it
-----------------------------------------------------------
''' 

import unittest
import testRun
import threading
import time
from deviceMock import MicroMock
from io import StringIO
import os


class Test(unittest.TestCase):

    def setUp(self):
        mock = MicroMock(1, self._testMethodName + "Mock.log")
        self.test = testRun.Test(mock)

    def tearDown(self):
        del self.test

    def testWriteParameters(self):
        '''
        Test Microcontroller configuration example
        '''    
        self.test.configureTest()
        assert( self.test.mode != testRun.DISABLED )
        
        self.test.OTAAparams("BE010000000000DF", "9ADE44A4AEF1CD77AEB44387BD976928")

        self.test.configureTest()
        assert( self.test.mode != testRun.DISABLED )

        self.test.ABPparams("01234567", "01234567890abcdef01234567890abcd", "01234567890abcdef01234567890abcd")

        self.test.configureTest()
        assert( self.test.mode != testRun.DISABLED )

    def testRunDevice(self):
        self.test.runTest()
        assert (self.test._rstate == 1)
        self.test.logFile.close()
        os.remove(self.test.logFile.name)
        
    def testPoll(self):
        self.test._rstate = 1
        self.test._logFile = StringIO()

        x = threading.Thread(target=self.test.poll, args = ())
        x.start()
        time.sleep(0.2)
        self.test._rstate = 0
        x.join(1)
        
        assert (self.test._rstate == 0)
        self.test._logFile.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testWriteParameters']
    unittest.main()