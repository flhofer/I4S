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
testLength = { "A": 5,  # Solo tests
               "B": 3,  # Unintentional disturbance
               "C": 5,  # Intentional disturbance
               "D": 0}

#Test parameters for all tests
#TODO: add values for changing parameters and variables
testParameters = [ # Test single device alone timing, all channels , ADR
                  { "testRun" : "A1",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1 },
                    "TestParam" : []
                    },
                  
                   # Test single device single channel resource, ADR
                  { "testRun" : "A2",
                     "NodeParam" : { "mode" : 2, "chnMsk" : 0x01, "conf" : 1 },
                     "TestParam" : []
                     },

                   # Test single channel, others around it are used, ADR
                  { "testRun" : "A3",
                    "NodeParam" :  { "mode" : 2, "chnMsk" : 0x02, "conf" : 1 },
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x05, "conf" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x05, "conf" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x05, "conf" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x05, "conf" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x05, "conf" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x05, "conf" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x05, "conf" : 0 }]},

                   # Test single channel, other data rates used, NO ADR
                  { "testRun" : "A4",
                    "NodeParam" :  { "mode" : 2, "chnMsk" : 0x01, "conf" : 1, "dataRate" : 0 },
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "dataRate" : 1 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "dataRate" : 2 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "dataRate" : 3 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "dataRate" : 4 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "dataRate" : 5 }]},

                   # Test single channel, other data rated + nearby used, NO ADR, + ADR nearby
                  { "testRun" : "A5",
                    "NodeParam" :  { "mode" : 2, "chnMsk" : 0x02, "conf" : 1, "dataRate" : 0 },
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x02, "conf" : 0, "dataRate" : 1 },
                                   { "mode" : 2, "chnMsk" : 0x02, "conf" : 0, "dataRate" : 2 },
                                   { "mode" : 2, "chnMsk" : 0x02, "conf" : 0, "dataRate" : 3 },
                                   { "mode" : 2, "chnMsk" : 0x02, "conf" : 0, "dataRate" : 4 },
                                   { "mode" : 2, "chnMsk" : 0x02, "conf" : 0, "dataRate" : 5 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x04, "conf" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x05, "conf" : 0 }]},

                   # Test single interference single channel same settings (mixing DR) with ADR
                  { "testRun" : "B1",
                    "NodeParam" :  { "mode" : 2, "chnMsk" : 0x01, "conf" : 1 },
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x01, "conf" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0 }]},
                  
                   # Test with reduced power..  A1 for non reduced power + obstacles
                  { "testRun" : "B2",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1, "power": 5 },
                    "TestParam" : []},
                  
                   # Test with default channels + nearby disturbing frequencies
                  { "testRun" : "B3",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0x07, "conf" : 1 },
                    "TestParam" : [{"mode" : 1, "freq" : 8680 },
                                   {"mode" : 1, "freq" : 8682 },
                                   {"mode" : 1, "freq" : 8684 },
                                   {"mode" : 1, "freq" : 8686 },]},

                   # Test default channels intentional obstruction
                  { "testRun" : "C1",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1 },
                    "TestParam" : [{"mode" : 1, "freq" : 8683, "dataLen": 242 },
                                   {"mode" : 1, "freq" : 8681, "dataLen": 242 },
                                   {"mode" : 1, "freq" : 8685, "dataLen": 242 },
                                   {"mode" : 1, "freq" : 8671, "dataLen": 242 },
                                   {"mode" : 1, "freq" : 8689, "dataLen": 242 },
                                   {"mode" : 1, "freq" : 8675, "dataLen": 242 },
                                   {"mode" : 1, "freq" : 8677, "dataLen": 242 },
                                   {"mode" : 1, "freq" : 8679, "dataLen": 242 },]},

                   # Test intentional collision, NO ADR
                  { "testRun" : "C2",
                    "NodeParam" :  { "mode" : 2, "chnMsk" : 0x07, "conf" : 1, "dataRate" : 0 },
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x07, "conf" : 0, "dataRate" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x07, "conf" : 0, "dataRate" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x07, "conf" : 0, "dataRate" : 0 }]},
                  
                   # Test run frequency exhaustion with ADR
                  { "testRun" : "C3",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1},
                    "TestParam" : [{"mode" : 2, "chnMsk" : 0xFF, "dataLen": 242, "usePB" : 1 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 242, "usePB" : 1 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 242, "usePB" : 1 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 242, "usePB" : 1 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 242, "usePB" : 1 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 242, "usePB" : 1 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 242, "usePB" : 1 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 242, "usePB" : 1 },]},

                   # Test run preamble exhaustion GW
                  { "testRun" : "C4",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1 },
                    "TestParam" : [{"mode" : 2, "chnMsk" : 0xFF, "dataLen": 0, "usePB" : 1 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 0, "usePB" : 1  },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 0, "usePB" : 1  },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 0, "usePB" : 1  },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 0, "usePB" : 1  },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 0, "usePB" : 1  },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 0, "usePB" : 1  },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 0, "usePB" : 1  },]},
                  
                   # Test NW server exhaustion -> Join flood
                  { "testRun" : "C5",
                    "NodeParam" : { "mode" : 2, "chnMsk" : 0xFF, "conf" : 1, "OTAA" : 1 },
                    "TestParam" : [{"mode" : 4, "chnMsk" : 0xFF, "conf" : 0 },
                                   {"mode" : 4, "chnMsk" : 0xFF, "conf" : 0 },
                                   {"mode" : 4, "chnMsk" : 0xFF, "conf" : 0 },
                                   {"mode" : 4, "chnMsk" : 0xFF, "conf" : 0 },
                                   {"mode" : 4, "chnMsk" : 0xFF, "conf" : 0 },
                                   {"mode" : 4, "chnMsk" : 0xFF, "conf" : 0 },
                                   {"mode" : 4, "chnMsk" : 0xFF, "conf" : 0 },
                                   {"mode" : 4, "chnMsk" : 0xFF, "conf" : 0 },]},
                  
                  #TODO: Class D tests
                ]

# Device parameters dictionary ordered by EUI
deviceParameters = {    "0123456789ABCDEF" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a30372e6008" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "3090FF8E", "APPSKEY": "9EEA9E2949847E280F95A318C58D80B7", "NWSKEY" : "1F4CC287FDEE8559F37EEF7281FDF4F7"},
                        "a8610a303933660b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "61C27FEC971BAA28BE94284DF5D7BA85", "DEVADDR" : "30650179", "APPSKEY": "ADE6499BDB90066663F82DC098D41A45", "NWSKEY" : "3F1CE1C1BB97E0E0D7A3B519D23569CB"},
                        "a8610a303925650b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a3037277e08" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},

                        "0004A30B002566B3" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a30392d6a0b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a303921670b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a3037329508" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},
                        "a8610a3039356a0b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "01234567", "APPSKEY": "01234567890abcdef01234567890abcd", "NWSKEY" : "01234567890abcdef01234567890abcd"},                     
                     }
        