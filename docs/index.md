## Welcome to the project website of I4S

The I4S project explores the challenges encountered when retrofitting or interconnecting a previously isolated system to a new Smart-* system-of-systems (SoS). Most of these challenges concern topics of security and resilience, affecting the stability and safety of an SoS. In a recently published book chapter (TSC2022), we process known security analyses and create a layer-based analysis of a Smart-Lighting system, our use case for the project. We elaborate on each element's possible issues and weaknesses and present some first actions to address them. However, it is a theoretical analysis and does thus not determine if these weaknesses are present.

To this aim, we experimentally explore through a common thread of performance their presence and the resilience of such a new system. We divided the project into three modules, connecting to the layers unique to a Smart-* system as follows:
- Communication: A LoRaWan infrastructure test assesses the resilience of a Smart-Lighting communication system
- Virtualization: Through an orchestration tool, we assess and attempt to manage the resilience of containerized real-time control applications
- Legacy testing: A testing framework we developed finally aids in assessing the weaknesses and testing the resilience of a legacy control software

This is just one repository of the I4S family. In the following, we detail components and modules for this project.


### Project dashboard for I4S

[Link](https://github.com/users/flhofer/projects/1)

### Contents of this main repository

The main repository contains scripts and Python code for the automated execution of the tests according to pre-established parameters. The code will be responsible for device management, communication, and parameter download to the connected micro-controllers.  
Please see the project documentation for further detail.

### I4S_LoRaWanNode

[Link](https://github.com/flhofer/I4S_LoRaWanNode)

The I4S* project investigates behavioral models of large-scale LoRaWan networks used in smart contexts. This repository contains the micro-controller code for a _Harward architecture_ micro-controller for end-node testing. The AVR micro-controller performs regular transmissions in different configurations to test the performance of the network and the communication reliability. Transmission time samples will describe the system's behavior and allow the creation of a model.

### I4S_LoRaWanTest

[Link](https://github.com/flhofer/I4S_LoRaWanTest)

Similar to the previous, this repository contains the micro-controller code for a _VN architecture_ micro-controller for end-node interference testing. The SamD micro-controller performs different kinds of transmissions to test the network's resilience. They embed thus an accessory role.
