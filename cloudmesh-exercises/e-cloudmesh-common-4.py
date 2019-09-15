from cloudmesh.common.Shell import Shell

#Develop a program that demonstartes the use of cloudmesh.common.Shell.
result = Shell.execute('pwd', witherror=False)
print(result)

result = Shell.ping(host = 'www.google.com')
print(result)

result = Shell.operating_system()
print(result)
