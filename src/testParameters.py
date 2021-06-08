''' 
-----------------------------------------------------------
Test Executor for the I4S performance testRun - Parameters

Created June, 8, 2021
(C) 2017-2021 Hofer Florian, Bolzano, ITALY
Released under GNU Public License (GPL)
email info@florianhofer.it
-----------------------------------------------------------
''' 

#defaults settings
testLength = { "A": 4,
               "B": 5,
               "C": 3,
               "D": 4}

#Test parameters for all tests
testParameters = [{ "testRun" : "A1",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1, "OTAA": 0 },
                    "TestParam" : []},

                  { "testRun" : "A2",
                    "TestParam" : [{"mode" : 1, "freq" : 8683 },
                                   {"mode" : 1, "freq" : 8681 },
                                   {"mode" : 1, "freq" : 8685 },
                                   {"mode" : 1, "freq" : 8671 },
                                   {"mode" : 1, "freq" : 8689 },
                                   {"mode" : 1, "freq" : 8675 },
                                   {"mode" : 1, "freq" : 8677 },
                                   {"mode" : 1, "freq" : 8679 },]},
                                                                          
                  { "testRun" : "A3",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1, "OTAA": 0 },
                    "TestParam" : [{"mode" : 1, "freq" : 8683 },
                                   {"mode" : 1, "freq" : 8681 },
                                   {"mode" : 1, "freq" : 8685 },
                                   {"mode" : 1, "freq" : 8671 },
                                   {"mode" : 1, "freq" : 8689 },
                                   {"mode" : 1, "freq" : 8675 },
                                   {"mode" : 1, "freq" : 8677 },
                                   {"mode" : 1, "freq" : 8679 },]},
                  
                  { "testRun" : "A4",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1, "OTAA": 0 },
                    "TestParam" : [{"mode" : 1, "freq" : 8683 },]},
                ]

# Device parameters dictionary ordered by EUI
deviceParameters = [{   "0123456789ABCDEF" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a30372e6008" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a303933660b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a303925650b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a3037277e08" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                     }]
        