from cloudmesh.common.util import banner, HEADING
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.variables import Variables

#Develop a program that demonstartes the use of banner, HEADING, and VERBOSE.

#banner use
banner("This is a banner")

#HEADING use
HEADING("This is a heading")

#VERBOSE use
variables = Variables()

variables['debug'] = True
variables['trace'] = True
variables['verbose'] = 10

dict = {"key1":"val1", "key2":"val2", "key3":"val3"}
VERBOSE(dict)