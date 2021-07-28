# I4S Project main repository
This repository contains scripts and instructions for the LoRaWan tests of the Smart-City network. Other repositories part of this project start with the same preamble `I4S_` and contain controller code and the like

## Run parameters

The primary python script `testMain.py` has to be run with the following parameters

* `-s` run in client mode (for connected test boxes), connects to IP+1
* `-S` run in server mode (for connected test boxes), should have client at IP-1
* `-e` skip x end-node micro-controllers when running tests
* `-t` skip x test-node micro-controllers when running tests
* `-d` target log directory, default `/tmp`
* `-l` target log prefix, default `test`
* `-i` select IP to bind to, default is the first device's IP 


To use two test boxes with each 1 end-node and four test-nodes, use the following command line combinations:

Test box 1  
`python3 testMain.py -s`

Test box 2  
`python3 testMain.py -S -e 1 -t 4`

The two boxes should be connected over adjacent IP addresses, e.g. `192.168.1.5` and `192.168.1.6`. However, in general you should use defaults and start the test with the provided `startTest.sh`.

## Start shell script options

The included shell scipt can be used for the following tasks:

* Start a test with the command `test` and the parameters of the Python script, in that order. The script will verify if necessary packages are installed
* Batch-program the connected micro-controllers with `program` selecting the desired controller type between `avr` and `mkr`. This step will use the binaries provided in the repository.
* Trigger a reset of all devices, with the `reset` command
* Clean temporary files with the `clean` command

In general the syntax is as follows:   
`./startTest.sh [command] [parameters]`
 
## Folders

    .
    ├── docs         # Project gp-pages website and other documents
    ├── src          # Python3 code for the test execution
    ├── test         # Python3 (unit) tests for the above code
    ├── binaries     # Micro-controller compiled binaries end/test node
    ├── startTest.sh # I4S test runner Bash script
    └── README.md    # this file
  
