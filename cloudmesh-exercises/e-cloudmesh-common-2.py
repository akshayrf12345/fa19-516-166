from cloudmesh.common.dotdict import dotdict

#Develop a program that demonstartes the use of dotdict.

dict = {"key1":"val1", "key2":"val2", "key3":"val3"}

dotted = dotdict(dict)

if dotted.key3 is "val3":
    print("Working as expected")
else:
    print("something went wrong")

