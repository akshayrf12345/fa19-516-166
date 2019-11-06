import requests
import numpy as np
from cloudmesh.mongo.CmDatabase import CmDatabase
from cloudmesh.common.console import Console
from datetime import datetime
from cloudmesh.compute.frugal import helpers

###########
###AZURE###
###########

def get_azure_pricing(refresh = False):

    cm = CmDatabase()
    azureinfo = cm.collection('azure-frugal')

    if azureinfo.estimated_document_count() > 0 and not refresh:
        Console.msg(f"Using local db azure flavors...")
        return azureinfo
    else:
        Console.msg(f"Pulling azure flavor price information...")
        azureinfo = requests.get('https://azure.microsoft.com/api/v3/pricing/virtual-machines/calculator/?culture=en-us&discount=mosp&v=20191002-1500-96990').json()
        azure_list = []
        for key,val in azureinfo['offers'].items():
            if type(val) is dict and 'cores' in val and 'ram' in val:
                cores = int(val['cores'])
                memory = int(val['ram'])
                if 'perhour' in val['prices']:
                    for location, value in val['prices']['perhour'].items():
                        if type(value['value']) is str:
                            print(value['value'])
                        azure_list.append(np.array(['Azure', key, location, int(cores), float(memory), float(value['value'])]))

    azureinfo = np.stack(azure_list, axis=0)
    azureinfo = helpers.format_mat(azureinfo)

    # convert to list of dicts
    azureinfo = azureinfo.to_dict('records')

    # write back to cm db
    for entry in azureinfo:
        entry["cm"] = {
            "kind": 'frugal',
            "driver": 'azure',
            "cloud": 'azure',
            "name": str(entry['machine-name'] + '-' + entry['region/location']),
            "updated": str(datetime.utcnow()),
        }

    Console.msg(f"Writing back to db ...")
    cm.update(azureinfo)

    return cm.collection('azure-frugal')
