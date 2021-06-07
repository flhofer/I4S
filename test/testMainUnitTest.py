'''
Created on 7 Jun 2021

@author: florianhofer
'''
import unittest
import testMain

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testParseTestsToRun(self):
        ''' Test commmand line test argument parsing '''
        
        tests = [
                [ [ "A1", "A2", "C1", "B4" ], [ "A1", "A2", "B4", "C1" ] ],
                [ [ "A*" ], [ "A1", "A2", "A3", "A4" ] ],                
                [ [ "A*", "C3" ], [ "A1", "A2", "A3", "A4", "C3" ] ],                                
                ]

        for inp,out in tests:
            self.assertListEqual(testMain.parseTestsToRun(inp), out)

        #TODO test for exception

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testParseTestsToRun']
    unittest.main()