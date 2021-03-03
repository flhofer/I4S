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
        echo "From PI : $line" 
    done
}

function waitDone() {
    port=${1:-'/dev/ttyUSB0'}

    while read line;
    do
        echo "From PI : $line" 

        if [ "$line" == "done" ]; then
            break;
        fi

    done
}

############################### cmd specific func ####################################

function runTest() {
    port=${1:-'/dev/ttyUSB0'}
    test=${2:-1}

    waitFree $port

    echo $test > $port

    waitDone $port
}

############################### cmd specific exec ####################################

# TODO
if [ $# -lt 1 ]; then
	echo "Not enough arguments supplied!"
	printUsage
fi

cmd=${1:-'test'}
shift

if [[ $cmd == "test" ]]; then
    tgrp=${1:-'A'}
    shift
    tno=${1:-'*'}
    shift

    setupSerial

    echo "TODO---"
else
    echo "Unknown command!!"
    printUsage
fi




