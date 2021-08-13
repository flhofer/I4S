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
testLength = { "A": 3,  # Solo tests
               "B": 3,  # Unintentional disturbance
               "C": 5,  # Intentional disturbance
               "D": 3,  # Distributed tests      
               }

nodeDlen  = [#0,         # No data
             1,         # "Some" data
#            11,        # Typical SL Low "Some" data
             16,        # Typical SL data
#            31,        # Typical SM data
             222]       # Max data for LoRaWan telegram running over a router, in binary Bytes -> HEX = *2
            #TODO: AVR v1.0.5 limits to 230 erroneously 

#Data rate from 0 - 7
maxDataLen = [ 51, 51, 51, 115, 242, 242, 242, 242 ]

#Test parameters for all tests
#TODO: add values for changing parameters and variables
testParameters = [
                   # 
                   # Group A, isolation tests, normal operation, w/o interfering in communication
                   #
                   
                   # Test single device alone timing, all channels , ADR
                  { "testRun" : "A1",
                    "NodeParam" : [{ "mode" : 2, "conf" : 1, "limit": 0 }],
                    "TestParam" : []
                    },
                  
                   # Test single device single channel resource, ADR
                  { "testRun" : "A2",
                     "NodeParam" : [{ "mode" : 2, "chnMsk" : 0x01, "conf" : 1, "limit": 0, "noReset": 1 }],
                     "TestParam" : []
                     },

                   # Test single channel, other data rates used, NO ADR, EX A4
                   # Default len 16
                  { "testRun" : "A3",
                    "NodeParam" : [{ "mode" : 2, "chnMsk" : 0x01, "dataRate" : 5, "conf" : 1 }],
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x01, "dataRate" : 1, "repeat" : 0, "rx1Delay" : 15000 },
                                   { "mode" : 2, "chnMsk" : 0x01, "dataRate" : 2, "repeat" : 0, "rx1Delay" : 15000 },
                                   { "mode" : 2, "chnMsk" : 0x01, "dataRate" : 3, "repeat" : 0, "rx1Delay" : 15000 },
                                   { "mode" : 2, "chnMsk" : 0x01, "dataRate" : 4, "repeat" : 0, "rx1Delay" : 15000 },
                                   { "mode" : 2, "chnMsk" : 0x01, "dataRate" : 0, "repeat" : 0, "rx1Delay" : 15000 }]},

                  #  # Test single channel, others around it are used, ADR
                  # Tested IV, does not have any effect
                  # { "testRun" : "A3",
                  #   "NodeParam" : [{ "mode" : 2, "chnMsk" : 0x02, "conf" : 1 }],
                  #   "TestParam" : [{ "mode" : 2, "chnMsk" : 0x05, "repeat" : 0 },
                  #                  { "mode" : 2, "chnMsk" : 0x05, "repeat" : 0 },
                  #                  { "mode" : 2, "chnMsk" : 0x05, "repeat" : 0 },
                  #                  { "mode" : 2, "chnMsk" : 0x05, "repeat" : 0 },
                  #                  { "mode" : 2, "chnMsk" : 0x05, "repeat" : 0 },
                  #                  { "mode" : 2, "chnMsk" : 0x05, "repeat" : 0 },
                  #                  { "mode" : 2, "chnMsk" : 0x05, "repeat" : 0 }]},

                   # Test single channel, other data rated + nearby used, NO ADR, + ADR nearby
                   # Tested IV, does not have any effect
                  # { "testRun" : "A5",
                  #   "NodeParam" : [{ "mode" : 2, "chnMsk" : 0x02, "conf" : 1, "dataRate" : 0 }],
                  #   "TestParam" : [{ "mode" : 2, "chnMsk" : 0x02, "dataRate" : 1, "repeat" : 0 },
                  #                  { "mode" : 2, "chnMsk" : 0x02, "dataRate" : 2, "repeat" : 0 },
                  #                  { "mode" : 2, "chnMsk" : 0x02, "dataRate" : 3, "repeat" : 0 },
                  #                  { "mode" : 2, "chnMsk" : 0x02, "dataRate" : 4, "repeat" : 0 },
                  #                  { "mode" : 2, "chnMsk" : 0x02, "dataRate" : 5, "repeat" : 0 },
                  #                  { "mode" : 2, "chnMsk" : 0x01, "repeat" : 0 },
                  #                  { "mode" : 2, "chnMsk" : 0x04, "repeat" : 0 },
                  #                  { "mode" : 2, "chnMsk" : 0x05, "repeat" : 0 }]},

                   # 
                   # Group B, involuntary collision or disturbance, coexistence -- normal operation with others using same network
                   #

                   # Test single interference single channel same settings (mixing DR) with ADR
                  { "testRun" : "B1",
                    "NodeParam" : [{ "mode" : 2, "chnMsk" : 0x01, "conf" : 0 }],
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x01, "repeat" : 0, "rx1Delay" : 15000 },
                                   { "mode" : 2, "chnMsk" : 0x01, "repeat" : 0, "rx1Delay" : 15000 },
                                   { "mode" : 2, "chnMsk" : 0x01, "repeat" : 0, "rx1Delay" : 15000 },
                                   { "mode" : 2, "chnMsk" : 0x01, "repeat" : 0, "rx1Delay" : 15000 },
                                   { "mode" : 2, "chnMsk" : 0x01, "repeat" : 0, "rx1Delay" : 15000 },
                                   { "mode" : 2, "chnMsk" : 0x01, "repeat" : 0, "rx1Delay" : 15000 },
                                   { "mode" : 2, "chnMsk" : 0x01, "repeat" : 0, "rx1Delay" : 15000 },
                                   { "mode" : 2, "chnMsk" : 0x01, "repeat" : 0, "rx1Delay" : 15000 }]},
                  
                   # Test with reduced power..  A1 for non reduced power + obstacles
                  { "testRun" : "B2",
                    "NodeParam" : [{"mode" : 2, "conf" : 1, "power": 5 }],
                    "TestParam" : []},
                  
                   # Test with default channels + nearby disturbing frequencies
                  { "testRun" : "B3",
                    "NodeParam" : [{"mode" : 2, "chnMsk" : 0x07, "conf" : 1 }],
                    "TestParam" : [{"mode" : 1, "freq" : 8680 }, # 250 / 125
                                   {"mode" : 1, "freq" : 8682 },
                                   {"mode" : 1, "freq" : 8684 },
                                   {"mode" : 1, "freq" : 8686 },]},

                   # 
                   # Group C, voluntary collision or disturbance, attacker
                   #

                   # Test default channels intentional obstruction
                  { "testRun" : "C1",
                    "NodeParam" : [{"mode" : 2, "conf" : 0 }],
                    "TestParam" : [{"mode" : 1, "freq" : 8683, "spreadFactor": 7, "codeRate": 5, "dataLen": 1 }, # = DR5, CR=LRW, DL1
                                   {"mode" : 1, "freq" : 8681, "spreadFactor": 7, "codeRate": 5, "dataLen": 1 },
                                   {"mode" : 1, "freq" : 8685, "spreadFactor": 7, "codeRate": 5, "dataLen": 1 },
                                   {"mode" : 1, "freq" : 8671, "spreadFactor": 7, "codeRate": 5, "dataLen": 1 },
                                   {"mode" : 1, "freq" : 8673, "spreadFactor": 7, "codeRate": 5, "dataLen": 1 },
                                   {"mode" : 1, "freq" : 8675, "spreadFactor": 7, "codeRate": 5, "dataLen": 1 },
                                   {"mode" : 1, "freq" : 8677, "spreadFactor": 7, "codeRate": 5, "dataLen": 1 },
                                   {"mode" : 1, "freq" : 8679, "spreadFactor": 7, "codeRate": 5, "dataLen": 1 },]},

                   # Test intentional collision, tx om evey channel
                  { "testRun" : "C2",
                    "NodeParam" : [{ "mode" : 2, "chnMsk" : 0xFF, "conf" : 0 }],
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x01, "dataRate" : 5, "dataLen": 1, "usePB" : 1, "repeat" : 0 }, # DR0 DR 5, same but LoRaWan
                                   { "mode" : 2, "chnMsk" : 0x02, "dataRate" : 5, "dataLen": 1, "usePB" : 1, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x04, "dataRate" : 5, "dataLen": 1, "usePB" : 1, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x08, "dataRate" : 5, "dataLen": 1, "usePB" : 1, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x10, "dataRate" : 5, "dataLen": 1, "usePB" : 1, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x20, "dataRate" : 5, "dataLen": 1, "usePB" : 1, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x40, "dataRate" : 5, "dataLen": 1, "usePB" : 1, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x80, "dataRate" : 5, "dataLen": 1, "usePB" : 1, "repeat" : 0 }]},
                                    
                   # Test run frequency air-time exhaustion with ADR
                  { "testRun" : "C3",
                    "NodeParam" : [{"mode" : 2, "conf" : 0 }],
                    "TestParam" : [{"mode" : 2, "dataLen": 242, "usePB" : 1, "dataRate" : 0, "repeat" : 0 },
                                   {"mode" : 2, "dataLen": 242, "usePB" : 1, "dataRate" : 0, "repeat" : 0 },
                                   {"mode" : 2, "dataLen": 242, "usePB" : 1, "dataRate" : 0, "repeat" : 0 },
                                   {"mode" : 2, "dataLen": 242, "usePB" : 1, "dataRate" : 0, "repeat" : 0 },
                                   {"mode" : 2, "dataLen": 242, "usePB" : 1, "dataRate" : 0, "repeat" : 0 },
                                   {"mode" : 2, "dataLen": 242, "usePB" : 1, "dataRate" : 0, "repeat" : 0 },
                                   {"mode" : 2, "dataLen": 242, "usePB" : 1, "dataRate" : 0, "repeat" : 0 },
                                   {"mode" : 2, "dataLen": 242, "usePB" : 1, "dataRate" : 0, "repeat" : 0 },]},

                   # Test run preamble exhaustion GW
                  { "testRun" : "C4",
                    "NodeParam" : [{"mode" : 2, "chnMsk" : 0xFF, "conf" : 1 }],
                    "TestParam" : [{"mode" : 1, "freq" : 8683, "dataLen": 0, "spreadFactor": 7, "codeRate": 5, "repeat" : 0, "simLWan": 1 },
                                   {"mode" : 1, "freq" : 8681, "dataLen": 0, "spreadFactor": 7, "codeRate": 5, "repeat" : 0, "simLWan": 1 },
                                   {"mode" : 1, "freq" : 8685, "dataLen": 0, "spreadFactor": 7, "codeRate": 5, "repeat" : 0, "simLWan": 1 },
                                   {"mode" : 1, "freq" : 8671, "dataLen": 0, "spreadFactor": 7, "codeRate": 5, "repeat" : 0, "simLWan": 1 },
                                   {"mode" : 1, "freq" : 8673, "dataLen": 0, "spreadFactor": 7, "codeRate": 5, "repeat" : 0, "simLWan": 1 },
                                   {"mode" : 1, "freq" : 8675, "dataLen": 0, "spreadFactor": 7, "codeRate": 5, "repeat" : 0, "simLWan": 1 },
                                   {"mode" : 1, "freq" : 8677, "dataLen": 0, "spreadFactor": 7, "codeRate": 5, "repeat" : 0, "simLWan": 1 },
                                   {"mode" : 1, "freq" : 8679, "dataLen": 0, "spreadFactor": 7, "codeRate": 5, "repeat" : 0, "simLWan": 1 },]},
                  
                   # Test NW server exhaustion -> Join flood
                  { "testRun" : "C5",
                    "NodeParam" : [{"mode" : 2, "conf" : 1, "OTAA" : 1 }],
                    "TestParam" : [{"mode" : 4, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 4, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 4, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 4, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 4, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 4, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 4, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 4, "usePB" : 1, "repeat" : 0 },]},

                   # 
                   # Group D, mixed tests, distributed setup
                   #
                  
                  # Test split boxes, Main closer to GW
                  { "testRun" : "D1",
                    "NodeParam" : [{ "mode" : 2, "chnMsk" : 0x01, "dataRate" : 5, "conf" : 1},
                                   { "mode" : 2, "chnMsk" : 0x01, "dataRate" : 1, "repeat" : 0, "rx1Delay" : 14000, "noStop": 1, "noDCycle": 1 }], # sets Rx1 and has 1s fixed Rx2 = 15s 
                    "TestParam" : [{ "mode" : 0 },
                                   { "mode" : 0 },
                                   { "mode" : 0 },
                                   { "mode" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x01, "dataRate" : 2, "repeat" : 0, "rx1Delay" : 15000 },
                                   { "mode" : 2, "chnMsk" : 0x01, "dataRate" : 3, "repeat" : 0, "rx1Delay" : 15000 },
                                   { "mode" : 2, "chnMsk" : 0x01, "dataRate" : 4, "repeat" : 0, "rx1Delay" : 15000 },
                                   { "mode" : 2, "chnMsk" : 0x01, "dataRate" : 0, "repeat" : 0, "rx1Delay" : 15000 }]},

                  # Test split boxes, Main closer to GW
                  { "testRun" : "D2",
                    "NodeParam" : [{"mode" : 2, "chnMsk" : 0x07, "conf" : 1, "limit": 0 }],
                    "TestParam" : [{"mode" : 0 },
                                   {"mode" : 0 },
                                   {"mode" : 0 },
                                   {"mode" : 0 },
                                   {"mode" : 1, "freq" : 8680 }, # 250 / 125
                                   {"mode" : 1, "freq" : 8682 },
                                   {"mode" : 1, "freq" : 8684 },
                                   {"mode" : 1, "freq" : 8686 },]},

                  { "testRun" : "D3",
                    "NodeParam" : [{"mode" : 2, "chnMsk" : 0x07, "conf" : 1, "limit": 0 }],
                    "TestParam" : [{"mode" : 0 },
                                   {"mode" : 0 },
                                   {"mode" : 0 },
                                   {"mode" : 0 },
                                   {"mode" : 1, "freq" : 8683, "spreadFactor": 7, "codeRate": 5, "dataLen": 1, "power": 5 },
                                   {"mode" : 1, "freq" : 8681, "spreadFactor": 7, "codeRate": 5, "dataLen": 1, "power": 5 },
                                   {"mode" : 1, "freq" : 8685, "spreadFactor": 7, "codeRate": 5, "dataLen": 1, "power": 5 },]},
                                 
                ]

        