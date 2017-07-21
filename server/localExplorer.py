import json

instruments = ['A','B','C','D','E','F','G','H','I','J','K','L']

def arch_to_array(architecture):
    array = [0] * 60
    arch = json.loads(architecture)
    for j in range(0,5):
        for i in range(0, 12):
            if instruments[i] in arch[j]:
                array[i+j*12] = 1
    return array

def array_to_arch(array):
    arch = '["'
    for j in range(0,5):
        for i in range(0, 12):
            if array[i+j*12] == 1:
                arch += instruments[i]
        if j < 4:
            arch += '","'
    arch += '"]'
    return arch

def permute_arch(arch):
    initialArray = arch_to_array(arch)
    res = []
    for i in range(60):
        modArray = initialArray[:]
        modArray[i] ^= 1
        res.append(array_to_arch(modArray))
    return res

if __name__ == '__main__':
    print "localExplorer"
    arch = '["A","B","C","D","E"]'
    res = permute_arch(arch)
    print res