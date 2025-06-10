import itertools
ct = 0
for x in itertools.product('АНТИУОПЯ', repeat=7):
    x = ''.join(x)
    #if 'АНТИУТОПИЯ' in x :
    ct += 1
    print(ct)
#281_474_976_710_656