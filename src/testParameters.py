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
               "D": 0,  # Distributed tests      
               }

nodeDlen  = [#0,         # No data
             1,         # "Some" data
             11,        # Typical SL Low "Some" data
             16,        # Typical SL data
#            31,        # Typical SM data
             230]       # Max data for LoRaWan telegram, in binary Bytes -> HEX = *2
            #TODO: AVR v1.0.5 limits to 230 erroneously 

#Data rate from 0 - 7
maxDataLen = [ 51, 51, 51, 115, 242, 242, 242, 242 ]

#Test parameters for all tests
#TODO: add values for changing parameters and variables
testParameters = [ # Test single device alone timing, all channels , ADR
                  { "testRun" : "A1",
                    "NodeParam" : [{ "mode" : 2, "chnMsk" : 0xFF, "conf" : 1 }],
                    "TestParam" : []
                    },
                  
                   # Test single device single channel resource, ADR
                  { "testRun" : "A2",
                     "NodeParam" : [{ "mode" : 2, "chnMsk" : 0x01, "conf" : 1 }],
                     "TestParam" : []
                     },

                   # Test single channel, others around it are used, ADR
                  { "testRun" : "A3",
                    "NodeParam" : [{ "mode" : 2, "chnMsk" : 0x02, "conf" : 1 }],
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x05, "conf" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x05, "conf" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x05, "conf" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x05, "conf" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x05, "conf" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x05, "conf" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x05, "conf" : 0, "repeat" : 0 }]},

                   # Test single channel, other data rates used, NO ADR
                  { "testRun" : "A4",
                    "NodeParam" : [{ "mode" : 2, "chnMsk" : 0x01, "conf" : 1, "dataRate" : 0 }],
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "dataRate" : 1, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "dataRate" : 2, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "dataRate" : 3, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "dataRate" : 4, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "dataRate" : 5, "repeat" : 0 }]},

                   # Test single channel, other data rated + nearby used, NO ADR, + ADR nearby
                  { "testRun" : "A5",
                    "NodeParam" : [{ "mode" : 2, "chnMsk" : 0x02, "conf" : 1, "dataRate" : 0 }],
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x02, "conf" : 0, "dataRate" : 1, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x02, "conf" : 0, "dataRate" : 2, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x02, "conf" : 0, "dataRate" : 3, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x02, "conf" : 0, "dataRate" : 4, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x02, "conf" : 0, "dataRate" : 5, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x04, "conf" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x05, "conf" : 0, "repeat" : 0 }]},

                   # Test single interference single channel same settings (mixing DR) with ADR
                  { "testRun" : "B1",
                    "NodeParam" : [{ "mode" : 2, "chnMsk" : 0x01, "conf" : 1 }],
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "conf" : 0, "repeat" : 0 }]},
                  
                   # Test with reduced power..  A1 for non reduced power + obstacles
                  { "testRun" : "B2",
                    "NodeParam" : [{"mode" : 2, "chnMsk" : 0xFF, "conf" : 1, "power": 5 }],
                    "TestParam" : []},
                  
                   # Test with default channels + nearby disturbing frequencies
                  { "testRun" : "B3",
                    "NodeParam" : [{"mode" : 2, "chnMsk" : 0x07, "conf" : 1 }],
                    "TestParam" : [{"mode" : 1, "freq" : 8680 },
                                   {"mode" : 1, "freq" : 8682 },
                                   {"mode" : 1, "freq" : 8684 },
                                   {"mode" : 1, "freq" : 8686 },]},

                   # Test default channels intentional obstruction
                  { "testRun" : "C1",
                    "NodeParam" : [{"mode" : 2, "chnMsk" : 0xFF, "conf" : 1 }],
                    "TestParam" : [{"mode" : 1, "freq" : 8683, "dataLen": 121 },
                                   {"mode" : 1, "freq" : 8681, "dataLen": 121 },
                                   {"mode" : 1, "freq" : 8685, "dataLen": 121 },
                                   {"mode" : 1, "freq" : 8671, "dataLen": 121 },
                                   {"mode" : 1, "freq" : 8689, "dataLen": 121 },
                                   {"mode" : 1, "freq" : 8675, "dataLen": 121 },
                                   {"mode" : 1, "freq" : 8677, "dataLen": 121 },
                                   {"mode" : 1, "freq" : 8679, "dataLen": 121 },]},

                   # Test intentional collision, NO ADR
                  { "testRun" : "C2",
                    "NodeParam" : [{ "mode" : 2, "chnMsk" : 0x07, "conf" : 1, "dataRate" : 0 }],
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x07, "conf" : 0, "dataRate" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x07, "conf" : 0, "dataRate" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x07, "conf" : 0, "dataRate" : 0, "repeat" : 0 }]},
                  
                   # Test run frequency exhaustion with ADR
                  { "testRun" : "C3",
                    "NodeParam" : [{"mode" : 2, "chnMsk" : 0xFF, "conf" : 1}],
                    "TestParam" : [{"mode" : 2, "chnMsk" : 0xFF, "dataLen": 121, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 121, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 121, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 121, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 121, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 121, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 121, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 121, "usePB" : 1, "repeat" : 0 },]},

                   # Test run preamble exhaustion GW
                  { "testRun" : "C4",
                    "NodeParam" : [{"mode" : 2, "chnMsk" : 0xFF, "conf" : 1 }],
                    "TestParam" : [{"mode" : 2, "chnMsk" : 0xFF, "dataLen": 0, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 0, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 0, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 0, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 0, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 0, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 0, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 0, "usePB" : 1, "repeat" : 0 },]},
                  
                   # Test NW server exhaustion -> Join flood
                  { "testRun" : "C5",
                    "NodeParam" : [{"mode" : 2, "chnMsk" : 0xFF, "conf" : 1, "OTAA" : 1 }],
                    "TestParam" : [{"mode" : 4, "chnMsk" : 0xFF, "conf" : 0, "repeat" : 0 },
                                   {"mode" : 4, "chnMsk" : 0xFF, "conf" : 0, "repeat" : 0 },
                                   {"mode" : 4, "chnMsk" : 0xFF, "conf" : 0, "repeat" : 0 },
                                   {"mode" : 4, "chnMsk" : 0xFF, "conf" : 0, "repeat" : 0 },
                                   {"mode" : 4, "chnMsk" : 0xFF, "conf" : 0, "repeat" : 0 },
                                   {"mode" : 4, "chnMsk" : 0xFF, "conf" : 0, "repeat" : 0 },
                                   {"mode" : 4, "chnMsk" : 0xFF, "conf" : 0, "repeat" : 0 },
                                   {"mode" : 4, "chnMsk" : 0xFF, "conf" : 0, "repeat" : 0 },]},
                  
                  #TODO: Class D tests
                ]

# Device parameters dictionary ordered by EUI - Test Devices, Test Application, Private network SN
deviceParameters = {    "1234567890ABCDEF" : {"APPEUI" : "ABCDEF1234567890", "APPKEY" : "ABCDEF1234567890ABCDEF1234567890", "DEVADDR" : "ABC12345", "APPSKEY": "ABCDEF1234567890ABCDEF1234567890", "NWSKEY" : "ABCDEF1234567890ABCDEF1234567890"},
                     }
        