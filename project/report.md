# Cloudmesh Frugal With AWS, Azure, and Google Cloud

Brian Funk

brfunk@iu.edu

[fa19-516-166](https://github.com/cloudmesh-community/fa19-516-166)

[Contributors](https://github.com/cloudmesh-community/fa19-516-166/graphs/contributors)

## Abstract

Cloudmesh frugal is a cloudmesh command for comparing the cost of compute for AWS, Azure, and GCP in various regions. It compares
price relative to the hardware specifications of the machines, an provide the VM with the best value. It has three core commands which
list, boot, and benchmark the cheapest vm.

## Introduction

Cloudmesh frugal collects pricing information on all of the availble flavors for AWS, GCP, and Azure. Those prices are then
compared to the physical specifications of the machine, which are then compared with each other. The core component of frugal is a
ranked list of flavors across the three compute providers, sorted by value. From this list, vms can be booted, and then benchmarked. 

## Usage

        """
        ::

            Usage:
                frugal list [-refresh] [--order=ORDER] [--size=SIZE]
                frugal boot [--refresh] [--order=ORDER]
                frugal benchmark

            Arguments:
              ORDER       sorting hierarchy, either price, cores, or
                          memory
              SIZE        number of results to be printed to the
                          console

            Options:
               --refresh         forces a refresh on all entries for
                                 aws, gcp, and azure
               --order=ORDER     sets the sorting on the results list
               --size=SIZE       sets the number of results returned
                                 to the console

            Description:
                frugal list
                    lists cheapest flavors for aws, azure, and gcp
                    in a sorted table

                frugal boot
                    boots the cheapest bootable vm from the frugal
                    list. Currently only supports azure and aws

                frugal benchmark
                    executes a benchmarking command on the newest
                    available vm on the current cloud

            Examples:


                 cms frugal list --refresh --order=price --size=150
                 cms frugal boot --order=memory
                 cms frugal benchmark

                 ...and so on
                 
            Tips:
                frugal benchmark will stall the command line after 
                the user enters their ssh key. This means the benchmark
                is running
                

            Limitations:

                frugal boot and benchmark are not supported for gcp



        """

## Design

Calling the cloudmesh frugal list command will first check to see if frugal information already exists in the local mongodb. If it is
does and the user does not signal for a refresh, then the local information is used. If the information does not exist for a provider
or the user signals for a refresh, then the flavor pricing information is pulled and processed into a frugal matrix. The frugal
is then saved back to the local mongodb, and then combined with the information of the other providers. It is then sorted, and the 
final frugal matrix is printed to the console. Calling frugal boot retrieves final table produces in frugal list, but does not
print it. Instead it filters the table to the providers that are usuable, and then boots the top ranked vm. Finally frugal benchmark
is designed to be used directly after frugal boot, as it uses the current cloud and the most recent vm. It sends a benchmarking file
to the vm via scp, runs the benchmark, prints the benchmark times, and then deletes the file.

### Architecture

This is a sketch of the logic flow of cloudmesh frugal list and boot. It is not comprehensive, but it gives a core understanding
of how the command works and interacts with the local db and the internet.
![Very rough architecture/design diagram](images/frugal_design.png){#fig:frugal_design}


## Benchmarks

There are two pytest files for frugal, test_01_frugal_list.py and test_02_frugal_boot.py. They collectively test frugal list, boot,
and benchmark.

## Work Breakdown

### Weekly Work Updates

#### Week of 9/29/19

Cloudmesh not entirely working at this point, began to explore AWS frugal example. Tested some urls to obtain the pricing info
from GCP and Azure. Needs to be cleaned, and will also likely need to be pushed into mongodb (not running yet). See AWS example. Code 
so far
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

#### Week of 11/17/19

Resolved an issue with not being able to boot up aws vms, which was hindering the frugal boot code. Now frugal boot works with aws,
and the structure is there for it to work with azure with a few tweaks. Currently having a few issues with getting an azure vm up
and running, but I'll try to figure that out during class time this week. After that I'll get Azure running and then start working
on PyTests and documentation. Hope to have that all done by the end of the weekend to give time to check over things

#### Week of 11/24/19

Completed Azure boot and frugal benchmark. Finalized documentation of code. Added pytests
