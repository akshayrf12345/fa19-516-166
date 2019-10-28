import requests
import pprint
import numpy as np
from cloudmesh.mongo.CmDatabase import CmDatabase

#mostly just gonna mess around here and experiment with pulling pricing information from different cloud services

###To Do###
#check to see if GCP, AWS, and Azure pricing exists in local mongodb, if not, pull using below functions


#cols for final price array will be as follows:
#[provider, machine_name, region/location, cores, memory, price]

#########
###AWS###
#########

def get_aws_pricing():
    cm = CmDatabase()

    awsstuff = cm.collection('aws-flavor')

    #need do do some kind of check for no AWS flavor

    #this assumes it exists in the mongo
    aws_list = []
    for x in awsstuff.find():
        print(x['attributes'])
        aws_list.append(np.array(['AWS', x['sku'], x['attributes']['location'], x['attributes']['vcpu'], x['attributes']['memory'], float(x['price']['pricePerUnit']['USD'])]))
    return np.stack(aws_list, axis=0)

print(get_aws_pricing())

############
###GOOGLE###
############

def get_google_pricing():
    googleinfo = requests.get('https://cloudpricingcalculator.appspot.com/static/data/pricelist.json?v=1570117883807').json()['gcp_price_list']
    google_list = []
    for machine,locations in googleinfo.items():
        if type(locations) is dict and 'cores' in locations and 'memory' in locations:
            cores = locations['cores']
            memory = locations['memory']
            for location in locations:
                #'cores' is end of regions, so stop if found
                if location == 'cores':
                    break
                else:
                    google_list.append(np.array(['GCP',machine,location,cores,memory,locations[location]]))
    return np.stack(google_list, axis=0)

###########
###AZURE###
###########

def get_azure_pricing():
    azureinfo = requests.get('https://azure.microsoft.com/api/v3/pricing/virtual-machines/calculator/?culture=en-us&discount=mosp&v=20191002-1500-96990').json()
    azure_list = []
    for key,val in azureinfo['offers'].items():
        if type(val) is dict and 'cores' in val and 'ram' in val:
            cores = int(val['cores'])
            memory = int(val['ram'])
            if 'perhour' in val['prices']:
                for location, value in val['prices']['perhour'].items():
                    azure_list.append(np.array(['Azure', key, location, cores, memory, float(value['value'])]))
    return np.stack(azure_list, axis=0)
#keys are dict_keys(['tiers', 'softwareLicenses', 'windowsTypes', 'linuxTypes', 'operatingSystems', 'billingOptions',
# 'sizesOneYear', 'sizesThreeYear', 'sizesPayGo', 'subscriptionOptions', 'offers', 'regions', 'discounts', 'resources', 'schema', 'skus'])

#pp = pprint.PrettyPrinter(indent=4)
#googlemat =get_google_pricing()
#azuremat = get_azure_pricing()
#pp.pprint(azuremat)
#pp.pprint(googlemat.shape)