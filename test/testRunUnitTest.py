'''
Created on 31 May 2021

@author: florianhofer
'''
import unittest
import testRun
from deviceMock import MicroMock


class Test(unittest.TestCase):


    def setUp(self):
        mock = MicroMock(1, "mock.log")
        self.test = testRun.Test(mock)

    def tearDown(self):
        del self.test

    def testWriteParameters(self):
        '''
        Test configuration example
        '''    
        print("Configure testRun")
        self.test.configureTest()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testWriteParameters']
    unittest.main()