import itertools
ct=0
for x in itertools.product ('0123456', repeat = 6):
    x = ''.join(x)
    if x[-1:] not in '0123' and x[0] != '0':
        print(x)
        if x.count('0') + x.count('2') + x.count('4') + x.count('6') == x.count('1') + x.count('3') +x.count('5') :
            ct += 1
print(ct)