## Welcome to the project website of I4S

The I4S project explores the challenges encountered when retrofitting or interconnecting a previously isolated system to a new Smart-* system-of-systems (SoS). Most of these challenges concern topics of security and resilience, affecting the stability and safety of an SoS. In a recently published book chapter (TSC2022), we process known security analyses and create a layer-based analysis of a Smart-Lighting system, our use case for the project. We elaborate on each element's possible issues and weaknesses and present some first actions to address them. However, it is a theoretical analysis and does thus not determine if these weaknesses are present.

To this aim, we experimentally explore through a common thread of performance their presence and the resilience of such a new system. We divided the project into three modules, connecting to the layers unique to a Smart-* system as follows:
- Communication: A LoRaWan infrastructure test assesses the resilience of a Smart-Lighting communication system
- Virtualization: Through an orchestration tool, we assess and attempt to manage the resilience of containerized real-time control applications
- Legacy testing: A testing framework we developed finally aids in assessing the weaknesses and testing the resilience of a legacy control software

This is just one repository of the I4S family. In the following, we detail components and modules for this project.


## Module Communication

This first module is composed of three repositories. The first [main](https://github.com/flhofer/I4S) repository is the same as this website hosting. It contains scripts and Python code for the automated execution of the tests according to pre-established parameters. The code will be responsible for device management, communication, and parameter download to the connected micro-controllers. The second and third repositories, described in the following, contain the code to be downloaded to the two used microcontrollers to execute the experiments.

For experimentation, we designed two setups as depicted in the following. The right setup serves as an in-vitro configuration to tune parameters (of the python script). The left side of the figure shows the on-site configuration. Please see the project documentation for further detail.

![Experiment setup](archExperiments.jpg)

The figure's test boxes contain each (end) node and four test nodes with the software below. A raspberry PI 3B+ acts as an execution agent and runs the python script of the principal repository. The two test boxes communicate via an ad-hoc WiFi connection.

<img src="LoraBox.jpg" alt="Test boxes" width="250"/><img src="LoraBox_inside.jpg" alt="Test boxes inside" width="250"/>

The [Project dashboard](https://github.com/users/flhofer/projects/1) contains issues and the next changes to address for this module. This does thus also include the microcontrollers of the two other repositories. 

The following [archive](https://bit.ly/3iIJRh7) contains the logs and results of the tests performed on the Smart-Lighting pilot project of the city of Merano.

### I4S_LoRaWanNode

[Link](https://github.com/flhofer/I4S_LoRaWanNode)

The I4S* project investigates behavioral models of large-scale LoRaWan networks used in smart contexts. This repository contains the micro-controller code for a _Harward architecture_ micro-controller for end-node testing. The AVR micro-controller performs regular transmissions in different configurations to test the performance of the network and the communication reliability. Transmission time samples will describe the system's behavior and allow the creation of a model.

### I4S_LoRaWanTest

[Link](https://github.com/flhofer/I4S_LoRaWanTest)

Similar to the previous, this repository contains the micro-controller code for a _VN architecture_ micro-controller for end-node interference testing. The SamD micro-controller performs different transmissions to test the network's resilience. They embed thus an accessory role.

## Module Virtualizzation

[Link](https://github.com/flhofer/real-time-containers)

## Module Legacy testing

[Link](https://github.com/flhofer/IEC_61131-3_TestLib)

