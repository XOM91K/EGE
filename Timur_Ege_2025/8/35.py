import itertools
k = 0
ct = 0
for x in itertools.product(sorted('КОМПАНИЯ'), repeat = 6):
    x = ''.join(x)
    k += 1
    #КИИИММ 33
    #КИИМИМ 34
    if x[0] != 'М' and x.count('И') == 3:
        if k % 2 != 0:
            ct += 1
            print(ct, k)