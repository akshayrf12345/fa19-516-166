# Cloudmesh Frugal With AWS, Azure, and Google Cloud

Brian Funk

brfunk@iu.edu

[fa19-516-166](https://github.com/cloudmesh-community/fa19-516-166)

## Abstract

Cloudmesh command for comparing the cost of compute for AWS, Azure, and GCP in various regions. It will compare price relative
to the hardware specifications of the machines, an provide the VM with the best value.

## Introduction

Cloudmesh Frugal will collect pricing information on all of the availble VMs for AWS, GCP, and Azure. Those prices will be
compared to the performance of the machine in benchmarking, which will then all be compared against each other. There is already
pricing information for AWS in Cloudmesh, which will be extended to GCP and Azure. The frugal benchmarks will compare them based
on hardware specs/price

## Design

Calling the frugal command (not yet designed/finalized) will first check to see if pricing information exists in the
local mongodb for AWS, GCP, and Azure flavors. As of of now, only the information only exists for AWS. If the information does
not exist, then it is pulled (and stored back into db? -join for if vm exists but not pricing?).Data will then be joined into
a single numpy area/pandas frame (depending on calculations tbd). Many of the dimensions of the VMs will be transformed by price
for benchmarking. The transformed table should also then be saved to the mongodb for memory? Or calc script will rerun since
pricing will stay in mongo? Once again tbd. Anyway, the best value vm will be returned. 

### Architecture

Below is an early sketch of the logic flow of cloudmesh frugal. It will likely be changed in final implemenetation, as this is
just an overview. 
![Very rough architecture/design diagram](images/frugal_design.png){#fig:frugal_design}

## Implementation

TBD

### Technologies Used

TBD

## Results

TBD

### Deployment Benchmarks

TBD

### Application Benchmarks

TBD

## Limitations

TBD

## Conclusion


## Work Breakdown

### TODO

* Implement cms commands to begin frugal code
* Capture and formet pricing info from GCP/Azure -see AWS implementation
* Service?
* Determine how benchmarking wil work (divide all by price?)
* PyTests
* Add more ToDos

### Weekly Work Updates

#### Week of 9/29/19

Cloudmesh not entirely working at this point, began to explore AWS frugal example. Tested some urls to obtain the pricing info
from GCP and Azure. Needs to be cleaned, and will also likely need to be pushed into mongodb (not running yet). See AWS example. Code so far
at [frugaltesting.py](https://github.com/cloudmesh-community/fa19-516-166/blob/master/project/frugaltesting.py)

#### Week of 10/6/19

Most of the week was spent getting Cloudmesh to run properly after bouncing back and forth from using Windows to Windows Subsystem.
Success on Window so will be using that for development entirely. Was able to get Chameleon VM up and running after some trials, so
which helped in understand of Cloudmesh command flow. No code updates

#### Week of 10/13/19

Currently reading documentation on OPENAPI and finalizing how that service will be integrated in frugal project. To be updated...
