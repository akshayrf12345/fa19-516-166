from cloudmesh.common.FlatDict import FlatDict

#Develop a program that demonstartes the use of FlatDict.

dict = {"name":"Brian",
        "age":23,
        "education": {"degree":"MSDS",
                      "credits":30},
        "hair color":"brown"}

flattened = FlatDict(dict)

print(flattened)