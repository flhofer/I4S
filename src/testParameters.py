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
               "C": 5,
               "D": 0}

#Test parameters for all tests
#TODO: add values for changing parameters and variables
testParameters = [{ "testRun" : "A1",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1, "OTAA": 0 },
                    "TestParam" : []
                    },

                  { "testRun" : "A2",
                    "NodeParam" :  { "mode" : 2, "chnMsk" : 0x80, "conf" : 1, "OTAA": 0 },
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x7F, "conf" : 0, "OTAA": 0 },
                                   { "mode" : 2, "chnMsk" : 0x7F, "conf" : 0, "OTAA": 0 },
                                   { "mode" : 2, "chnMsk" : 0x7F, "conf" : 0, "OTAA": 0 },
                                   { "mode" : 2, "chnMsk" : 0x7F, "conf" : 0, "OTAA": 0 },
                                   { "mode" : 2, "chnMsk" : 0x7F, "conf" : 0, "OTAA": 0 },
                                   { "mode" : 2, "chnMsk" : 0x7F, "conf" : 0, "OTAA": 0 },
                                   { "mode" : 2, "chnMsk" : 0x7F, "conf" : 0, "OTAA": 0 }]},

                  { "testRun" : "A3",
                    "NodeParam" :  { "mode" : 2, "chnMsk" : 0x01, "conf" : 1, "OTAA": 0, "dataRate" : [0,0] },
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : [1,1] },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : [2,2] },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : [3,3] },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : [4,4] },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : [5,5] }]},

                  { "testRun" : "A4",
                    "NodeParam" :  { "mode" : 2, "chnMsk" : 0x01, "conf" : 1, "OTAA": 0, "dataRate" : [0,0] },
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : [1,1] },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : [2,2] },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : [3,3] },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : [4,4] },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : [5,5] },
                                   { "mode" : 2, "chnMsk" : 0x02, "conf" : 0, "OTAA": 0 },
                                   { "mode" : 2, "chnMsk" : 0x04, "conf" : 0, "OTAA": 0 },
                                   { "mode" : 2, "chnMsk" : 0x07, "conf" : 0, "OTAA": 0 }]},

                  { "testRun" : "B1",
                    "NodeParam" :  { "mode" : 2, "chnMsk" : 0x01, "conf" : 1, "OTAA": 0 },
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0 }]},
                  
                  { "testRun" : "B2",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1, "OTAA": 0, "power": 0 },
                    "TestParam" : []},
                  
                  { "testRun" : "B3",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1, "OTAA": 0, "power": 0 },
                    "TestParam" : []},
                  
                  { "testRun" : "B4",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1, "OTAA": 0, "power": 0 },
                    "TestParam" : []},
                  
                  { "testRun" : "B5",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0x01, "conf" : 1, "OTAA": 0 },
                    "TestParam" : [{"mode" : 1, "freq" : 8682 },
                                   {"mode" : 1, "freq" : 8684 },]},

                  { "testRun" : "C1",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0x01, "conf" : 1, "OTAA": 0 },
                    "TestParam" : [{"mode" : 1, "freq" : 8683 },]},

                  { "testRun" : "C2",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0x01, "conf" : 1, "OTAA": 0, "dataRate" : [0,0] },
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : [0,0] },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : [0,0] },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : [0,0] }]},
                  
                  { "testRun" : "C3",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1, "OTAA": 0 },
                    "TestParam" : [{"mode" : 1, "freq" : 8683, "dataLen": 252 },
                                   {"mode" : 1, "freq" : 8681, "dataLen": 252  },
                                   {"mode" : 1, "freq" : 8685, "dataLen": 252  },
                                   {"mode" : 1, "freq" : 8671, "dataLen": 252  },
                                   {"mode" : 1, "freq" : 8689, "dataLen": 252  },
                                   {"mode" : 1, "freq" : 8675, "dataLen": 252  },
                                   {"mode" : 1, "freq" : 8677, "dataLen": 252  },
                                   {"mode" : 1, "freq" : 8679, "dataLen": 252  },]},

                  { "testRun" : "C4",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1, "OTAA": 0 },
                    "TestParam" : [{"mode" : 1, "freq" : 8683, "dataLen": 0 },
                                   {"mode" : 1, "freq" : 8681, "dataLen": 0  },
                                   {"mode" : 1, "freq" : 8685, "dataLen": 0  },
                                   {"mode" : 1, "freq" : 8671, "dataLen": 0  },
                                   {"mode" : 1, "freq" : 8689, "dataLen": 0  },
                                   {"mode" : 1, "freq" : 8675, "dataLen": 0  },
                                   {"mode" : 1, "freq" : 8677, "dataLen": 0  },
                                   {"mode" : 1, "freq" : 8679, "dataLen": 0  },]},
                  
                  #TODO: verify join mask
                  { "testRun" : "C5",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1, "OTAA": 0 },
                    "TestParam" : [{"mode" : 2, "chnMsk" : 0xFF, "conf" : 0, "OTAA": 0, "joinRepeat" : 1 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "conf" : 0, "OTAA": 0, "joinRepeat" : 1 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "conf" : 0, "OTAA": 0, "joinRepeat" : 1 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "conf" : 0, "OTAA": 0, "joinRepeat" : 1 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "conf" : 0, "OTAA": 0, "joinRepeat" : 1 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "conf" : 0, "OTAA": 0, "joinRepeat" : 1 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "conf" : 0, "OTAA": 0, "joinRepeat" : 1 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "conf" : 0, "OTAA": 0, "joinRepeat" : 1 },]},
                  
                  #TODO: Class D tests
                ]

# Device parameters dictionary ordered by EUI
deviceParameters = [{   "0123456789ABCDEF" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a30372e6008" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a303933660b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a303925650b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a3037277e08" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                     }]
        