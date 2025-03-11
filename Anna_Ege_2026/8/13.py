import itertools
k = 0
for x in itertools.product('0123456', repeat = 6):
    if x[0] != '0' and x[-1] >= '4' and x.count('0') + x.count('2') + x.count('4') + x.count('6') == x.count('1') + x.count('3') + x.count('5') :
        k += 1
print(k)