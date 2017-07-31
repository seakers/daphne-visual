import math
import random

def dist2(p1, p2):
    return (70000*p1["x"]-70000*p2["x"])**2 + (p1["y"]-p2["y"])**2

in_filename = "data1_2.csv"
out_filename = "data2_2.csv"
lines = [line.rstrip() for line in open(in_filename)]

f = open(out_filename, 'w')

data = []

for line in lines:
    array = line.split(":")
    data.append({"architecture":array[0],"x":float(array[1]),"y":float(array[2])})

ret = []
n = len(data)
taken = [False]*n
for i in range(n):
    if not taken[i]:
        taken[i] = True
        for j in range(i+1,n):
            if dist2(data[i],data[j]) < 80000: #50000
                taken[j] = True
        ret.append(data[i])

for line in ret:
    if line["y"] < 9500:
        f.write(line["architecture"]+":"+str(line["x"])+":"+str(line["y"])+"\n")

f.close()