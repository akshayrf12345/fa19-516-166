import pandas as pd
import numpy as np
from cloudmesh.common.Printer import Printer
from cloudmesh.frugal.api import aws_frugal, gcp_frugal, azure_frugal
from cloudmesh.compute.aws import Provider as awsProvider
from cloudmesh.common.console import Console
from cloudmesh.common.variables import Variables
from cloudmesh.vm.command.vm import VmCommand

class Manager(object):

    def __init__(self):
        print("init {name}".format(name=self.__class__.__name__))

    def list(self,order='price', resultssize=50, refresh=False, printit = True):
        # AWS pricing info
        aws = list(aws_frugal.get_aws_pricing(refresh=refresh).find())

        # GCP pricing info
        gcp = list(gcp_frugal.get_google_pricing(refresh=refresh).find())

        # azure pricing info
        azure = list(azure_frugal.get_azure_pricing(refresh=refresh).find())

        # combine the all of the pricing information and turn into pandas dataframe
        flavor_mat = aws + gcp + azure

        flavor_frame = pd.DataFrame(flavor_mat)[
            ['provider', 'machine-name', 'region/location', 'cores', 'core/price', 'memory', 'memory/price', 'price']]
        flavor_frame = flavor_frame.replace([np.inf, -np.inf], np.nan).dropna()

        if order == 'cores':
            flavor_frame = flavor_frame.sort_values(by=['core/price'], ascending=False)
        elif order == 'memory':
            flavor_frame = flavor_frame.sort_values(by=['memory/price'], ascending=False)
        elif order == 'price':
            flavor_frame = flavor_frame.sort_values(by=['price'], ascending=True)
        else:
            # TODO need to raise some kind of error here...actually should probably do sooner in method
            print('uhoh')

        # print out list of price tables things
        if printit:
            print(Printer.write(flavor_frame.head(resultssize).to_dict('records'),
                                order=['provider', 'machine-name', 'region/location', 'cores', 'core/price', 'memory',
                                       'memory/price', 'price']))
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


