'''
Created on 7 Jun 2021

@author: florianhofer
'''
import unittest
import testMain
from testMain import NotEnoughMicrosError

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testParseTestsToRun(self):
        ''' Test commmand line test argument parsing '''
        
        #Overwrite defaults to keep test consistent
        testMain.testLength = {
            "A": 3,
            "B": 2,
            "C": 1,
            "D": 4
            }
        
        tests = [
                [ [ "A1", "A2", "C1", "B2" ], [ "A1", "A2", "B2", "C1" ] ],
                [ [ "A*" ], [ "A1", "A2", "A3" ] ],                
                [ [ "A*", "C1" ], [ "A1", "A2", "A3", "C1" ] ],
                [ None , ["A1", "A2", "A3", "B1", "B2", "C1", "D1", "D2", "D3", "D4"] ]                       
                ]

        for inp,out in tests:
            self.assertListEqual(testMain.parseTestsToRun(inp), out)

        #test for exception
        with self.assertRaises(LookupError):
            testMain.parseTestsToRun(["A3", "B4", "C1"])

        with self.assertRaises(ValueError):
            testMain.parseTestsToRun(["A3", "B4D", "C1"])
            
    def testPrepareTest(self):
        
        with self.assertRaises(ValueError):
            testMain.prepareTest("")

        with self.assertRaises(NotEnoughMicrosError):
            testMain.prepareTest("A1")

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testParseTestsToRun']
    unittest.main()