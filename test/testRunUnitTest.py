'''
Created on 31 May 2021

@author: florianhofer
'''
import unittest
import testRun
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

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testWriteParameters']
    unittest.main()