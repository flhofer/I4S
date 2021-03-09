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

function getNextTestNos(){
    for i in ${!groups[@]}; do
        if [ $testGrp = ${groups[$i]} ]; then
            tno=($(seq  1 ${tests[$i]} ))
            break
        fi
    done
}

function getNextTest(){

    if [ -z $testGrp ]; then
        if [ $tgrp = "ALL" ]; then
            tgrp=(${groups[@]})
        else
            eval IFS=',' read -r -a tgrp <<< $tgrp
        fi
        testGrp=${tgrp[0]}
        if [ $tno = "ALL" ]; then 
            getNextTestNos
        else
            eval IFS=',' read -r -a tno <<< $tno
        fi
    else
        for i in ${!groups[@]}; do
            if [ $testGrp = ${groups[$i]} ]; then
                if [ $testNo -ge ${tests[$i]} ]; then
                    # goto next test, pop 
                    unset tgrp[0]
                    tgrp=( ${tgrp[@]} )
                    testGrp=${tgrp[0]}
                    if [ -z $tgrp ]; then
                        echo $tgrp
                        return 1
                    fi
                    getNextTestNos
                else
                    unset tno[0]
                    tno=( ${tno[@]} )
                    if [ -z $tno ]; then
                        echo $tno
                        return 1
                    fi
                fi
                break
            fi
        done
    fi
    # save to next test variables
    testGrp=${tgrp[0]}
    testNo=${tno[0]}
    return 0
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
    tno=${1:-'ALL'}
    shift

    setupSerial
	
    while getNextTest 
    do
        echo Test $testGrp $testNo
    done

else
    echo "Unknown command!!"
    printUsage
fi




