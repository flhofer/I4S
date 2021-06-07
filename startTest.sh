#!/bin/bash
#use bash, zsh or compatible -> wildcard conditions make it NOT posix compliant!

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

PYTHON3="python3"


############################### device comm functions ####################################


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

############################### Functions, generic ####################################

function printUsage() {

	cat <<EOF

Usage: $0 test [-r] [-d workdir] [-l logprefix] [group/number] .. [group/number] 
 or    $0 [prepcmd]
 
ex.    $0 test A2 B*  

where:

group     test group to execute: [ A, B, C, D, * ]
number		test numbers to execute, e.g. "A1 B2 D3", use * for all
prepcmd		prep command to execute: [clean, reset]

Defaults are:
group = A     execute test group A
number = *		execute all tests

EOF
	exit 1	
}

function checkLibraries(){
	eval "pip list | grep -F pyserial > /dev/null"
	if [ "$?" -eq 0 ] ; then
		return 0
	else
	    return 1
	fi
}

function createRamDisk() {
    echo "Creating RamDisk for logs"
    mkdir -P /dev/ramlog
    mount -t tmpfs -o size=128m tmpfs /mnt/ramlog
}

#if [ $# -lt 1 ]; then
#	echo "Not enough arguments supplied!"
#	printUsage
#fi

cmd=${1:-'test'}
shift

if [[ $cmd == "test" ]]; then

	checkLibraries
	if [ "$?" -ne 0 ]; then
		echo "Required Python libraries not present and/or installable."
		echo "Refer to README for details"
		exit 1
	fi
	
    # setupSerial 	# not needed anymore 
    # createRamDisk	# Maybe needed to save flash mem
	eval $PYTHON3 testMain.py $@

elif [[ $cmd == "clean" ]]; then
	echo "Not implemented"
	exit 1

elif [[ $cmd == "reset" ]]; then
	echo "Not implemented"
	exit 1
		
else
    echo "Unknown command!!"
    printUsage
fi
