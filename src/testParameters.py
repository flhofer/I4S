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
                    "NodeParam" :  { "mode" : 2, "chnMsk" : 0x01, "conf" : 1, "OTAA": 0, "dataRate" : 0 },
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : 1 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : 2 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : 3 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : 4 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : 5 }]},

                  { "testRun" : "A4",
                    "NodeParam" :  { "mode" : 2, "chnMsk" : 0x01, "conf" : 1, "OTAA": 0, "dataRate" : 0 },
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : 1 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : 2 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : 3 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : 4 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "OTAA": 0, "dataRate" : 5 },
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
                  
                
                  { "testRun" : "C5",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0x07, "conf" : 1, "OTAA": 0 },
                    "TestParam" : [{"mode" : 4, "chnMsk" : 0x07, "conf" : 0, "OTAA": 0 },
                                   {"mode" : 4, "chnMsk" : 0x07, "conf" : 0, "OTAA": 0 },
                                   {"mode" : 4, "chnMsk" : 0x07, "conf" : 0, "OTAA": 0 },
                                   {"mode" : 4, "chnMsk" : 0x07, "conf" : 0, "OTAA": 0 },
                                   {"mode" : 4, "chnMsk" : 0x07, "conf" : 0, "OTAA": 0 },
                                   {"mode" : 4, "chnMsk" : 0x07, "conf" : 0, "OTAA": 0 },
                                   {"mode" : 4, "chnMsk" : 0x07, "conf" : 0, "OTAA": 0 },
                                   {"mode" : 4, "chnMsk" : 0x07, "conf" : 0, "OTAA": 0 },]},
                  
                  #TODO: Class D tests
                ]

# Device parameters dictionary ordered by EUI
deviceParameters = [{   "0123456789ABCDEF" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a30372e6008" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "3090FF8E", "APPSKEY": "9EEA9E2949847E280F95A318C58D80B7", "NWSKEY" : "1F4CC287FDEE8559F37EEF7281FDF4F7"},
                        "a8610a303933660b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "61C27FEC971BAA28BE94284DF5D7BA85", "DEVADDR" : "30650179", "APPSKEY": "ADE6499BDB90066663F82DC098D41A45", "NWSKEY" : "3F1CE1C1BB97E0E0D7A3B519D23569CB"},
                        "a8610a303925650b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a3037277e08" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                     }]
        