import pandas as pd
import numpy as np
from cloudmesh.common.Printer import Printer
from cloudmesh.frugal.api import aws_frugal, gcp_frugal, azure_frugal

class Manager(object):

    def __init__(self):
        print("init {name}".format(name=self.__class__.__name__))

    def list(self,order='price', resultssize=50, refresh=False):
        print(order)
        print(refresh)
        print(resultssize)
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
            flavor_frame = flavor_frame.sort_values(by=['core/price'], ascending=False).head(resultssize).to_dict(
                'records')
        elif order == 'memory':
            flavor_frame = flavor_frame.sort_values(by=['memory/price'], ascending=False).head(resultssize).to_dict(
                'records')
        elif order == 'price':
            flavor_frame = flavor_frame.sort_values(by=['price'], ascending=True).head(resultssize).to_dict('records')
        else:
            # TODO need to raise some kind of error here...actually should probably do sooner in method
            print('uhoh')

        # print out list of price tables things
        print(Printer.write(flavor_frame,
                            order=['provider', 'machine-name', 'region/location', 'cores', 'core/price', 'memory',
                                   'memory/price', 'price']))

        return