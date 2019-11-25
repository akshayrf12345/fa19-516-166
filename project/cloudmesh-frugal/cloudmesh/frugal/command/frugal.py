from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.shell import Shell
from cloudmesh.common.console import Console
import pandas as pd
import numpy as np
from cloudmesh.common.Printer import Printer
from cloudmesh.frugal.api import aws_frugal, gcp_frugal, azure_frugal
from cloudmesh.compute.aws import Provider as awsProvider
from cloudmesh.compute.azure import Provider as azureProvider
from cloudmesh.common.variables import Variables
from cloudmesh.vm.command.vm import VmCommand
from cloudmesh.mongo.CmDatabase import CmDatabase
from os import path

class FrugalCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_frugal(self, args, arguments):
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
                    executes a benchmarking command on a vm, it
                    assumes that the vm has already been booted.

            Examples:


                 put examples here...



        """
        arguments.REFRESH = arguments['--refresh'] or None
        arguments.RESULTSSIZE = arguments['--size'] or None
        arguments.ORDER = arguments['--order'] or None

        if arguments.ORDER is None:
            arguments.ORDER='price'

        if arguments.REFRESH is None:
            arguments.REFRESH=False
        else:
            arguments.REFRESH=True

        if arguments.SIZE is None:
            arguments.SIZE=25


        if arguments.list:
            self.list(order = arguments.ORDER,refresh =bool(arguments.REFRESH), resultssize= int(arguments.SIZE))

        if arguments.boot:
            self.boot(order = arguments.ORDER,refresh =bool(arguments.REFRESH))

        if arguments.benchmark:
            self.benchmark()

        return ""

    def list(self,order='price', resultssize=50, refresh=False, printit = True):

        #check to make sure that order is either price, cores, or memory
        if order not in ['price', 'cores', 'memory']:
            Console.error(f'order argument must be price, cores, or memory')
            return

        # get aws pricing info
        aws = list(aws_frugal.get_aws_pricing(refresh=refresh).find())

        # get gcp pricing info
        gcp = list(gcp_frugal.get_google_pricing(refresh=refresh).find())

        # get azure pricing info
        azure = list(azure_frugal.get_azure_pricing(refresh=refresh).find())

        # combine the all of the pricing information and into a single numpy array
        flavor_mat = aws + gcp + azure

        # turn numpy array into a pandas dataframe, assign column names, and remove na values
        flavor_frame = pd.DataFrame(flavor_mat)[
            ['provider', 'machine-name', 'location', 'cores', 'core/price', 'memory', 'memory/price', 'price']]
        flavor_frame = flavor_frame.replace([np.inf, -np.inf], np.nan).dropna()

        # sort the dataframe by order
        if order == 'cores':
            flavor_frame = flavor_frame.sort_values(by=['core/price'], ascending=False)
        elif order == 'memory':
            flavor_frame = flavor_frame.sort_values(by=['memory/price'], ascending=False)
        else:
            flavor_frame = flavor_frame.sort_values(by=['price'], ascending=True)

        # print out the dataframe if printit, print results limited by resultssize
        if printit:
            print(Printer.write(flavor_frame.head(resultssize).to_dict('records'),
                                order=['provider', 'machine-name', 'location', 'cores', 'core/price', 'memory',

                                       'memory/price', 'price']))
        # return the final sorted data frame
        return flavor_frame

    def boot(self,order='price', refresh=False):
        Console.msg(f"Checking to see which providers are bootable ...")
        reachdict = {}

        #try to connect to aws
        try:
            from cloudmesh.compute.aws import Provider as awsProvider
            awsinst = awsProvider.Provider(name='aws', configuration="~/.cloudmesh/cloudmesh.yaml")
            Console.msg(f"aws reachable ...")
            reachdict['aws'] = awsinst
        except:
            Console.msg(f"aws not available ...")
        #try to connect to azure
        try:
            from cloudmesh.compute.azure import Provider as azureProvider
            azureinst = azureProvider.Provider(name='azure', configuration="~/.cloudmesh/cloudmesh.yaml")
            Console.msg(f"azure reachable ...")
            reachdict['azure'] = azureinst
        except:
            Console.msg(f"azure not available ...")
        #try to connect to gcp
        try:
            from cloudmesh.compute.gcp import Provider as gcpProvider
            gcpinst = gcpProvider.Provider(name='gcp', configuration="~/.cloudmesh/cloudmesh.yaml")
            Console.msg(f"gcp reachable ...")
            reachdict['gcp'] = gcpinst
        except:
            Console.msg(f"gcp not available ...")

        flavorframe = self.list(order, 10000000, refresh, printit=False)
        keysya = list(reachdict.keys())
        flavorframe = flavorframe[flavorframe['provider'].isin(keysya)]
        Console.msg(f"Showing top 5 options, booting first option now...")
        converted = flavorframe.head(5).to_dict('records')
        print(Printer.write(converted))
        cheapest = converted[0]
        var_list = Variables(filename="~/.cloudmesh/var-data")
        var_list['cloud'] = cheapest['provider']
        print('new cloud is ' + var_list['cloud'] + ', booting up the vm with flavor ' + cheapest['machine-name'])
        vmcom = VmCommand()
        vmcom.do_vm('boot --flavor=' + cheapest['machine-name'])
        return

    def benchmark(self):
        Console.msg(f'checking if a vm is running')
        """
        # get active cloud
        var_list = Variables(filename="~/.cloudmesh/var-data")
        current_cloud = var_list['cloud']

        # check to see if that cloud has an available vm
        cm = CmDatabase()
        print(current_cloud)
        vms = cm.collection(current_cloud + '-vm')
        activevms = list(vms.find({'status': 'available'}))
        print(activevms)
        if len(activevms) == 0:
            Console.error(f'no available vms...')
            return
        activevm = activevms[-1]

        #get key for the vm
        keyname=activevm['key']
        key_collection = cm.collection('local-key')
        keys = list(key_collection.find({'name' : keyname}))
        if len(keys) == 0:
            Console.error(f'key for vm does not exist in local db...')
            return
        mykey = keys[0]

        #get file path of the benchmark
        filepath = path.dirname(path.dirname(path.abspath(__file__))) + '/api/benchmark.py'
        filepath = filepath.replace('\\','/')

        #move the benchmark file to the vm
        print('-i ' + mykey['path'] + ' ubuntu@' + activevm['public_ips'] + ':' + filepath + ' /.')
        return
        Shell.scp('-i ' + mykey['path'] + ' ubuntu@' + activevm['public_ips'] + ':' + filepath + ' /.')
        """
        # get file path of the benchmark
        filepath = path.dirname(path.dirname(path.abspath(__file__))) + '/api/benchmark.py'
        filepath = filepath.replace('\\', '/')

        # prepare command to run the file
        vmcom = VmCommand()
        print('put ' + filepath + ' /home/ubuntu')
        vmcom.do_vm('put ' + filepath + ' /home/ubuntu')

        try:
            print('ssh --command=\"chmod +x benchmark.py;benchmark.py;exit\"')
            vmcom.do_vm('ssh --command=\"chmod +x benchmark.py;./benchmark.py;exit\"')
        except:
            Console.msg(f'could not ssh into vm, make sure one is running and reachable')
        print('todo - report times here')
