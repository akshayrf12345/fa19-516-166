# Cloudmesh Frugal With AWS, Azure, and Google Cloud

Brian Funk

brfunk@iu.edu

[fa19-516-166](https://github.com/cloudmesh-community/fa19-516-166)

[Contributors](https://github.com/cloudmesh-community/fa19-516-166/graphs/contributors)

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

add Docker information (see Piazza post 354)

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
* add Azure proper to frugal
* frugal boot - need to actually boot instead of just limit
* pytest for how long it takes to do various frugal cmd commands
* some kind of benchmark for a booted machine that measures the actually speed
* lastly I need to do some kind of Docker test or something?

### Questions moving forward

* When to write back to mongodb? IE should GCP and Azure flavors be written back to mongodb? Compute for those two clouds
  are in development so might have to wait until those are further along before worrying about them
* Keep everything in frugal.py or move GCP and Azure get pricing functions to other directories much like AWS currently is? Once
  again this will depend on other developments to Cloudmesh
* GCP has an api to get pricing but it needs a key...how to use with cloudmesh/is this okay?

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

Currently reading documentation on OPENAPI and thinking about how that service will be integrated in frugal project.
Updated report with all new progress, and Google pricing is completed in
[frugaltesting.py](https://github.com/cloudmesh-community/fa19-516-166/blob/master/project/frugaltesting.py), and it is done without
using the API. It uses a simplified JSON from their calculator. The file is parsed into the general structure that will be used for
benchmarking, a 2d numpy array with features [provider, machine name, region, cores, memory, and price]. Next up will be doing the
same with Azure.

#### Week of 10/20/19

Azure is complete as well, read into same template as GCP. Started Mongo as well but ran into issue with YAML file for the MODE of
the Mongo - ended the week...

#### Week of 10/27/19

Amazon info connected from Mongo, is now parsed into matrix. going to start working on Mongo refresh checks/downloads

#### Week of 11/03/19

Prep for demo at end of week with Gregor. Started to actually pull everything together. Flipped the frugal testing file into an
base class with a list method. Now have separate frugal files for aws, gcp, and azure that return a price matrix for each one. Built
in logic for it to save back to the db, as well as an argument for a refresh. Wrapping up integration for it to be called from
the cloudmesh console. Console implementation completed. All that is left is frugal boot, which will require some checks

#### Week of 11/10/19

Was not able to make too much progress this week because of other assignments. Frugal boot now has a command line interface. For now
it doesn't boot anything, but I worked on logic so that it filters the table to providers that can actually be booted. For now this
is only AWS but it should work with Azure once I incorporate a few more things. Otherwise I am now looking at the cloudmesh code to
figure out what information I need to boot a vm. Hope to have all of that done by the end of next week so I can begin to add tests.
