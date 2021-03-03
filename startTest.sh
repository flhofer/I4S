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

# TODO
if [ $# -lt 1 ]; then
	echo "Not enough arguments supplied!"
	printUsage
fi
