from cloudmesh.common.StopWatch import StopWatch
import time

#Develop a program that demonstartes the use of cloudmesh.common.StopWatch.
StopWatch.start("time check")
time.sleep(5)
StopWatch.stop("time check")

print(StopWatch.get("time check"))