'''
Created on 7 Jun 2021

@author: florianhofer
'''
import unittest
import testMain
import testRun
from testMain import NotEnoughMicrosError
from deviceMock import MicroMock

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testParseTestsToRun(self):
        ''' Test command line test argument parsing '''
        
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
                [ [] , ["A1", "A2", "A3", "B1", "B2", "C1", "D1", "D2", "D3", "D4"] ]                       
                ]

        for inp,out in tests:
            self.assertListEqual(testMain.parseTestsToRun(inp), out)

        #test for exception
        with self.assertRaises(LookupError):
            testMain.parseTestsToRun(["A3", "B4", "C1"])

        with self.assertRaises(ValueError):
            testMain.parseTestsToRun(["A3", "B4D", "C1"])
            
    def testPrepareTest(self):
        
        testMain.testParameters = [{ "testRun" : "A1",
                                     "NodeParam" : [],
                                     "TestParam" :[{"mode" : 1, "freq" : 8683 },
                                                   {"mode" : 1, "freq" : 8681 },
                                                   {"mode" : 1, "freq" : 8685 },
                                                   {"mode" : 1, "freq" : 8671 },
                                                   {"mode" : 1, "freq" : 8689 },
                                                   {"mode" : 1, "freq" : 8675 },
                                                   {"mode" : 1, "freq" : 8677 },
                                                   {"mode" : 1, "freq" : 8679 } ],
                                    }]
        
        # Test exceptions
        with self.assertRaises(ValueError):
            testMain.prepareTest("")

        with self.assertRaises(NotEnoughMicrosError):
            testMain.prepareTest("A1")

        #Test normal op
        for i in range(8):
            testMain.testers.append(testRun.Test(i,MicroMock(1, "testEmtpyMock.log")))
        
        testMain.prepareTest("A1");
        
        for tester in testMain.testers:
            self.assertEqual(1, tester.mode )
    
    def testGenerateParameters(self):
        
        testMain.testParameters = [{ "testRun" : "A1",
                             "NodeParam" :[{"mode" : 2, "chnMsk" : 0xFF, "conf" : 1, 'dataRate': [0,5]}],
                             "TestParam" :[{"mode" : 1, "freq" : 8683, 'dataLen': [0, 64, 242] },
                                           {"mode" : 1, "freq" : 8681 },
                                           {"mode" : 1, "freq" : 8685, 'repeat': 2, 'dataRate': [0,4]},
                                           {"mode" : 1, "freq" : 8671 },
                                           {"mode" : 1, "freq" : 8689 },
                                           {"mode" : 1, "freq" : 8675 },
                                           {"mode" : 1, "freq" : 8677 },
                                           {"mode" : 1, "freq" : 8679 } ],
                            }]
        
        tests = []
        for params in testMain.testParameters[0]["NodeParam"]:
            nodeT = testMain.generateVarParam(params)
            if nodeT != []:
                tests.append(nodeT)

        for params in testMain.testParameters[0]["TestParam"]:
            nodeT = testMain.generateVarParam(params)
            if nodeT != []:
                tests.append(nodeT)

        self.assertEqual(tests, [ [{'dataRate' : 0}, {'dataRate': 5}],
                                  [{'dataLen'  : 0}, {'dataLen' : 64}, {'dataLen': 242}],
                                  [{'dataRate' : 0}, {'dataRate': 4}]])
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testParseTestsToRun']
    unittest.main()