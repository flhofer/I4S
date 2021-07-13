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
                    "NodeParam" : [{ "mode" : 2, "chnMsk" : 0x07, "conf" : 1, "dataRate" : 0 }],
                    "TestParam" : [{ "mode" : 2, "chnMsk" : 0x07, "conf" : 0, "dataRate" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x07, "conf" : 0, "dataRate" : 0, "repeat" : 0 },
                                   { "mode" : 2, "chnMsk" : 0x07, "conf" : 0, "dataRate" : 0, "repeat" : 0 }]},
                  
                   # Test run frequency exhaustion with ADR
                  { "testRun" : "C3",
                    "NodeParam" : [{"mode" : 2, "chnMsk" : 0xFF, "conf" : 1}],
                    "TestParam" : [{"mode" : 2, "chnMsk" : 0xFF, "dataLen": 242, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 242, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 242, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 242, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 242, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 242, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 242, "usePB" : 1, "repeat" : 0 },
                                   {"mode" : 2, "chnMsk" : 0xFF, "dataLen": 242, "usePB" : 1, "repeat" : 0 },]},

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
deviceParameters = {    "0004A30B0021DD46" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "1DF36C5E60E406AAE2579775964C0BEF", "DEVADDR" : "30EF74EC", "APPSKEY": "A80CC27D2DF1FDFBC2DB396452A70FA8", "NWSKEY" : "F62FC9E3AFD31F47985F8DCBE604751B"},
                        "a8610a30372e6008" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "9ADE44A4AEF1CD77AEB44387BD976928", "DEVADDR" : "3090FF8E", "APPSKEY": "9EEA9E2949847E280F95A318C58D80B7", "NWSKEY" : "1F4CC287FDEE8559F37EEF7281FDF4F7"},
                        "a8610a303933660b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "61C27FEC971BAA28BE94284DF5D7BA85", "DEVADDR" : "31C9027E", "APPSKEY": "3C902260AFC98E7EADCE8380FACD49F7", "NWSKEY" : "47FE6B1F09AB8670A0A7E5FE857ED103"},
                        "a8610a303925650b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "2F8E8A0D759C5321DEDBD0A08A269E77", "DEVADDR" : "30682796", "APPSKEY": "C998106AFE78036485458D825DE8B8DB", "NWSKEY" : "67FE23972522566370FDE30CF2DC9469"},
                        "a8610a3037277e08" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "80DB8A2E17FA422293CBD67DCCA5DC40", "DEVADDR" : "3158EDFE", "APPSKEY": "2617160089DD50FE39CE37A5609BB3B6", "NWSKEY" : "7A2F6BE6D1375CAE004CE9366924BDD9"},

                        "0004A30B002566B3" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "08E56DE8F675E9A4DD0D97E11EB7D205", "DEVADDR" : "30FCB30F", "APPSKEY": "361DCF38BBA1AAC2C487D72425C5803F", "NWSKEY" : "E4104197CB061418D291034CA489E56B"},
                        "a8610a30392d6a0b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "717DB4D3AB6E1A7B1D9646C6538CA428", "DEVADDR" : "31E562AF", "APPSKEY": "E1D292E90DC0F5637AFC563168740141", "NWSKEY" : "90A75BDDA87DEDDC26B7E534C8A2EA9A"},
                        "a8610a303921670b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "3B423CCEE012CDDA0500498CEBABD29E", "DEVADDR" : "30A376BA", "APPSKEY": "8264A2AD1D997A08D0E45D3C6EA1711E", "NWSKEY" : "65DFCFC48EF9D148AB18BEF76ACA7DF2"},
                        "a8610a3037329508" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "21D00E5BEC3004F36FA6004327EA10CC", "DEVADDR" : "31704506", "APPSKEY": "036828DC638138F6782E2D0899697180", "NWSKEY" : "8194BD94108D0F8E13E427F3CF904EA5"},
                        "a8610a3039356a0b" : {"APPEUI" : "BE010000000000DF", "APPKEY" : "CFC0A401DB07BFC4C2B5D3754B0FF904", "DEVADDR" : "311C9726", "APPSKEY": "A93E73810ED56A609A5E1DCF88E4ED4F", "NWSKEY" : "D7DBFDC6C2E3BD60ACD1D1A8BBF245B6"},                     
                     }
        