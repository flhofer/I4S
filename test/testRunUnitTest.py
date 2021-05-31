'''
Created on 31 May 2021

@author: florianhofer
'''
import unittest
import testRun
import threading
import time
from deviceMock import MicroMock


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
        
    def testPoll(self):
        self.test._rstate = 1
        x = threading.Thread(target=self.test.poll, args = ())
        x.start()
        time.sleep(1)
        self.test._rstate = 0
        x.join(1)
        assert (self.test._rstate == 0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testWriteParameters']
    unittest.main()