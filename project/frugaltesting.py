import requests
import pprint

#mostly just gonna mess around here and experiment with pulling pricing information from different cloud services

############
###GOOGLE###
############

#this works...but the info is limited. Not exactly the comprehensive list I'm looking for
googleinfo = requests.get('https://cloudpricingcalculator.appspot.com/static/data/pricelist.json?v=1570117883807').json()

#also an api documented at
#https://cloud.google.com/billing/v1/how-tos/catalog-api

###########
###AZURE###
###########

azureinfo = requests.get('https://azure.microsoft.com/api/v3/pricing/virtual-machines/calculator/?culture=en-us&discount=mosp&v=20191002-1500-96990').json()
#keys are dict_keys(['tiers', 'softwareLicenses', 'windowsTypes', 'linuxTypes', 'operatingSystems', 'billingOptions',
# 'sizesOneYear', 'sizesThreeYear', 'sizesPayGo', 'subscriptionOptions', 'offers', 'regions', 'discounts', 'resources', 'schema', 'skus'])

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(azureinfo['offers'])