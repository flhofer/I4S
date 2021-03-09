#!/bin/bash

if [[ ! "$1" == "quiet" ]]; then

cat <<EOF
::::::::::: :::     ::::::::  
    :+:    :+:     :+:    :+: 
    +:+   +:+ +:+  +:+        
    +#+  +#+  +:+  +#++:++#++ 
    +#+ +#+#+#+#+#+       +#+ 
    #+#       #+#  #+#    #+# 
###########   ###   ########  
    Smart System testing

EOF

else 
	shift
fi

############################### global variables ####################################

#Initialization
baudRate=9600
groups=('A' 'B' 'C' 'D')
tests=(4 3 5 0)
testNo=
testGrp=

############################### Functions, generic ####################################

function printUsage() {

	cat <<EOF

Usage: $0 test [-r] [group] [number]
 or    $0 [prepcmd] 

where:

group     test group to execute: [ A, B, C, D, * ]
number		test numbers to execute, e.g. "1,2,3", * for all
prepcmd		prep command to execute: [clean, reset]

Defaults are:
group = A     execute test group A
number = *		execute all tests

EOF
	exit 1	
}

function setupSerial() {

    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # ...

        for port in /dev/ttyUSB* ; do
            [ -e "$port" ] || continue
            stty $baudRate -F $port raw -echo
        done
        for port in /dev/ttyACM* ; do
            [ -e "$port" ] || continue
            stty $baudRate -F $port raw -echo
        done

    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Mac OSX

        for port in /dev/cu.usbmodem* ; do
            [ -e "$port" ] || continue
            stty -f $port $baudRate raw -echo
        done

    fi
}

function createRamDisk() {
    echo "Creating RamDisk for logs"
    mkdir -P /dev/ramlog
    mount -t tmpfs -o size=128m tmpfs /mnt/ramlog
}

function waitFree() {
    port=${1:-'/dev/ttyUSB0'}

    while read line;
    do
        echo "$(date): $line" 
    done
}

function waitDone() {
    port=${1:-'/dev/ttyUSB0'}

    while read line;
    do
        echo "$(date): $line" 

        if [ "$line" == "done" ]; then
            break;
        fi

    done
}

function getNextTest(){

    if [[ "$testGrp" == "" ]]; then
        #tgrp=("${tgrp[@]/,/ }")
        #tno=("${tno[@]/,/ }")
        eval IFS=',' read -r -a tgrp <<< $tgrp
        eval IFS=',' read -r -a tno <<< $tno
        testGrp=${tgrp[0]}
        testNo=${tno[0]}
        echo ${tno[@]}
    else
        for i in ${!groups[@]}; do
            if [[ "$testGrp" -eq "${[$i]}" ]]; then
                if [[ "$testNo" -ge "${tests[$i]}" ]]; then
                    # goto next test
                    testGrp=${groups[${i+1}]}
                    testNo=1
                else
                    testNo=$(( $testNo + 1 ))
                fi
                break
            fi
        done
    fi

}

############################### cmd specific func ####################################

function runTest() {
    port=${1:-'/dev/ttyUSB0'}
    grp=${2:-'A'}
    test=${3:-1}

    waitFree $port

    echo g${grp}t${test}r > $port

    waitDone $port
}

############################### cmd specific exec ####################################

# if [ $# -lt 1 ]; then
# 	echo "Not enough arguments supplied!"
# 	printUsage
# fi

cmd=${1:-'test'}
shift

if [[ $cmd == "test" ]]; then
    tgrp=${1:-'A'}
    shift
    tno=${1:-'*'}
    shift

    setupSerial

    getNextTest
    echo Test $testGrp $testNo
    getNextTest
    echo Test $testGrp $testNo
    getNextTest
    echo Test $testGrp $testNo
    getNextTest
    echo Test $testGrp $testNo
    getNextTest
    echo Test $testGrp $testNo
    getNextTest
    echo Test $testGrp $testNo
    getNextTest
    echo Test $testGrp $testNo
    getNextTest
    echo Test $testGrp $testNo
    getNextTest
    echo Test $testGrp $testNo
    
    exit

    while getNextTest ;
    do
        echo Test $testGrp $testNo
    done

else
    echo "Unknown command!!"
    printUsage
fi




