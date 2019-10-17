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

The Google Cloud Platform and Azure 

### Architecture

TBD

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
from GCP and Azure. Needs to be cleaned, and will also likely need to be pushed into vm class. See AWS example. Code so far
at [frugaltesting.py](/frugaltesting.py)

#### Week of 10/6/19

Most of the week was spent getting Cloudmesh to run properly after bouncing back and forth from using Windows to Windows Subsystem.
Success on Window so will be using that for development entirely. Was able to get Chameleon VM up and running after some trials, so
which helped in understand of Cloudmesh command flow. No code updates

#### Week of 10/13/19

Currently reading documentation on OPENAPI and finalizing how that service will be integrated in frugal project. To be updated...
