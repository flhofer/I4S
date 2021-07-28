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
ports=( )
testFile="binaries/LoRaWanTest.bin"
nodeFile="binaries/LoRaWanNode.hex"
bossac="~/.arduino15/packages/arduino/tools/bossac/1.7.0-arduino3/bossac"
avrdudeD="$HOME/.arduino15/packages/arduino/tools/avrdude/6.3.0-arduino17"
avrdude="${avrdudeD}/bin/avrdude"

############################### device comm functions ####################################


function updateAVR() {
	port=${1:-""} 
	eval "${avrdude} -C${avrdudeD}/etc/avrdude.conf -patmega32u4 -cavr109 -P${port} -b57600 -D -Uflash:w:${nodeFile}:i" 
	
}


function updateMKR() {
	port=${1:-""} 
	eval ${bossac} --port=${port} -U true -i -e -w -v ${testFile} -R 
}

function resetSerial() {
	port=$1
	sleep 1
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # ...
        stty "1200" -F $port

    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Mac OSX
        stty -f $port "1200"   
    fi
	while true ; do
        sleep 0.5
        [ -c "${port}" ] && break
    done
}

function setupSerial() {

    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # ...

        for port in /dev/ttyUSB* ; do
            [ -e "$port" ] || continue
            ports+=($port)
            stty $baudRate -F $port raw -echo
        done
        for port in /dev/ttyACM* ; do
            [ -e "$port" ] || continue
            ports+=($port)
            stty $baudRate -F $port raw -echo
        done

    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Mac OSX

        for port in /dev/cu.usbmodem* ; do
            [ -e "$port" ] || continue
            ports+=($port)
            stty -f $port $baudRate raw -echo        
        done

    fi
}

############################### Functions, generic ####################################

function printUsage() {

	cat <<EOF

Usage: $0 test [-rsS] [-i <ip>] [-d <workdir>] [-l <logprefix>] [group/number] .. [group/number] 
 or    $0 test [-rsS] [-i <ip>] [--dir=<workdir>] [--log=<logprefix>] [group/number] .. [group/number] 
 or    $0 [prepcmd]
 
ex.    $0 test A2 B*  

where:

group     test group to execute: [ A, B, C, D, * ]
number		test numbers to execute, e.g. "A1 B2 D3", use * for all
prepcmd		prep command to execute: [clean, reset, program]

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
	eval $PYTHON3 src/testMain.py $@

	# move results if in tmp dir to disk
	eval mkdir -p results
	eval mv /tmp/*.log results/

elif [[ $cmd == "clean" ]]; then
	eval rm -rf ./src/__pycache__

elif [[ $cmd == "reset" ]]; then
	setupSerial
	
	for port in ${ports[@]} ; do
		echo "Resetting ${port}..."
		resetSerial $port
	done
elif [[ $cmd == "program" ]]; then
	if [[ -z "$1" ]]; then
		echo "Select the type of device to program, 'avr' or 'mkr'"
		echo "e.g. $0 program avr"
	fi

	setupSerial
	
    echo ${ports[@]}
 
    if [[ "$1" == "avr" ]] ; then
		for port in ${ports[@]} ; do
			resetSerial $port
			updateAVR $port
		done
	fi
	if [[ "$1" == "mkr" ]] ; then 
		for port in ${ports[@]} ; do
			resetSerial $port
			updateMKR $port
		done
	fi
else
    echo "Unknown command!!"
    printUsage
fi
