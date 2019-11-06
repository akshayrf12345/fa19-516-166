import pandas as pd
import numpy as np
from cloudmesh.common.Printer import Printer
from cloudmesh.compute.frugal import aws_frugal, gcp_frugal, azure_frugal

class frugal(object):

    def __init__(self):
        pass

    def list(self, order = 'cores', resultssize = 25):
        #AWS pricing info
        aws = list(aws_frugal.get_aws_pricing().find())

        #GCP pricing info
        gcp = list(gcp_frugal.get_google_pricing().find())

        #azure pricing info
        azure = list(azure_frugal.get_azure_pricing().find())

        #combine the all of the pricing information and turn into pandas dataframe
        flavor_mat = aws + gcp + azure

        flavor_frame = pd.DataFrame(flavor_mat)[['provider', 'machine-name', 'region/location', 'cores', 'core/price', 'memory', 'memory/price', 'price']]
        flavor_frame = flavor_frame.replace([np.inf, -np.inf], np.nan).dropna()

        if order == 'cores':
            flavor_frame = flavor_frame.sort_values(by=['core/price'], ascending=False).head(resultssize).to_dict('records')
        elif order == 'memory':
            flavor_frame = flavor_frame.sort_values(by=['memory/price'], ascending=False).head(resultssize).to_dict('records')
        else:
            #need to raise some kind of error here...actually should probably do sooner in method
            print('uhoh')

        #print out list of price tables things
        print(Printer.write(flavor_frame, order = ['provider', 'machine-name', 'region/location', 'cores', 'core/price', 'memory', 'memory/price', 'price']))


        return 'temp'


#cols for final price array will be as follows:
#[provider, machine_name, region/location, cores, memory, price]


goob = frugal()
goob.list(order = 'memory', resultssize=50)
