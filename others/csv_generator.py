import math
import random
import itertools
import websocket
import json
import numpy as np
from VASSAR import VASSAR

orbits = [1, 2]
instruments = ['A','B','C','D']

# Functions

orbits_c = [1, 2, 3, 4, 5]
instruments_c = ['A','B','C','D','E','F','G','H','I','J','K','L']

def arch_to_array(architecture):
    array = [0] * 60
    arch = json.loads(architecture)
    for j in range(0,5):
        for i in range(0, 12):
            if instruments_c[i] in arch[j]:
                array[i+j*12] = 1
    return array

def array_to_arch(array):
    arch = '["'
    for j in range(0,5):
        for i in range(0, 12):
            if array[i+j*12] == 1:
                arch += instruments_c[i]
        if j < 4:
            arch += '","'
    arch += '"]'
    return arch

def dist2(p1, p2):
    return (50000*p1["x"]-50000*p2["x"])**2 + (p1["y"]-p2["y"])**2

# Main script

out_filename1 = "data1.csv"
out_filename2 = "data2.csv"

print "Step 1\n"

array_mask = [1]*60
for o in range(len(orbits_c)):
    if orbits_c[o] not in orbits:
        array_mask[o*12:o*12+12] = [0]*12
for i in range(len(instruments_c)):
    if instruments_c[i] not in instruments:
        for o in range(4):
            array_mask[i+o*12] = 0
index = [i for i,x in enumerate(array_mask) if x == 1]
perm = list(itertools.product([0, 1], repeat=len(index)))

print "Architecture to compute: %d\n" % len(perm)

print "Step 2\n"

f = open(out_filename1, 'w')
vassar = VASSAR.VASSAR()

count = 0
for elem in perm:
    # Create architecture
    array = [0]*60
    for i in range(len(index)):
        array[index[i]] = elem[i]
    arch = array_to_arch(array)
    # Compute science and cost
    result = vassar.evaluateArch(json.loads(arch))
    # Write result to file
    f.write(arch+":"+str(result["science"])+":"+str(result["cost"])+"\n")
    print "Computed: %d/%d" % count, len(perm)
    count += 1
f.close()