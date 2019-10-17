import requests
import pprint
import numpy as np

#mostly just gonna mess around here and experiment with pulling pricing information from different cloud services

###TODO##
#check to see if GCP, AWS, and Azure pricing exists in local mongodb, if not, pull using below functions


#cols for final price array will be as follows:
#[provider, machine_name, region/location, cores, memory, price]

############
###GOOGLE###
############

def get_google_pricing():
    googleinfo = requests.get('https://cloudpricingcalculator.appspot.com/static/data/pricelist.json?v=1570117883807').json()['gcp_price_list']
    google_list = []
    provider = 'GCP'
    for machine,locations in googleinfo.items():
        if type(locations) is dict and 'cores' in locations and 'memory' in locations:
            cores = locations['cores']
            memory = locations['memory']
            for location in locations:
                #'cores' is end of regions, so stop if found
                if location == 'cores':
                    break
                else:
                    google_list.append(np.array([provider,machine,location,cores,memory,locations[location]]))
    return np.stack(google_list, axis=0)

#also an api documented at
#https://cloud.google.com/billing/v1/how-tos/catalog-api
#^ requires api key I'm not sure if this is good?

###########
###AZURE###
###########

def get_azure_pricing():
    azureinfo = requests.get('https://azure.microsoft.com/api/v3/pricing/virtual-machines/calculator/?culture=en-us&discount=mosp&v=20191002-1500-96990').json()
    #do some things
    return azureinfo
#keys are dict_keys(['tiers', 'softwareLicenses', 'windowsTypes', 'linuxTypes', 'operatingSystems', 'billingOptions',
# 'sizesOneYear', 'sizesThreeYear', 'sizesPayGo', 'subscriptionOptions', 'offers', 'regions', 'discounts', 'resources', 'schema', 'skus'])

pp = pprint.PrettyPrinter(indent=4)
googlemat =get_google_pricing()
pp.pprint(googlemat.shape)