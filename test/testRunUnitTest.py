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
  
        self.test.mode = 0
        self.test.configureTest()
        self.assertNotEqual(self.test.mode, testRun.DISABLED )
        self.assertListEqual( self.test._micro.buffer , ["m0l16\n"])

        self.test._micro.clearBuffer()
        
        self.test.mode = 1
        self.test.configureTest()
        self.assertNotEqual(self.test.mode, testRun.DISABLED )
        self.assertListEqual( self.test._micro.buffer , ["m1f8683b125s12c8l16\n"])

        self.test._micro.clearBuffer()
        
        self.test.mode = 2
        self.test.OTAAparams("BE010000000000DF", "9ADE44A4AEF1CD77AEB44387BD976928")
        self.test.configureTest()
        self.assertNotEqual(self.test.mode, testRun.DISABLED )
        self.assertListEqual( self.test._micro.buffer , ["m2our1CFFhp1d255l16\n", "EBE010000000000DFh\n", "K9ADE44A4AEF1CD77AEB44387BD976928h\n"])

        self.test._micro.clearBuffer()
               
        self.test.ABPparams("01234567", "01234567890abcdef01234567890abcd", "01234567890abcdef01234567890abcd")
        self.test.configureTest()
        self.assertNotEqual(self.test.mode, testRun.DISABLED )
        self.assertListEqual( self.test._micro.buffer , ["m2aur1CFFhp1d255l16\n", "D01234567h\n", "N01234567890ABCDEF01234567890ABCDh\n", "A01234567890ABCDEF01234567890ABCDh\n"])

    def testRunDevice(self):
        self.test.runTest()
        self.assertEquals(self.test._rstate, 1)
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
        
        self.assertEquals (self.test._rstate, 0)
        self.test._logFile.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testWriteParameters']
    unittest.main()