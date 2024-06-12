import itertools
ct =0
for x in itertools.product('0123456', repeat=7):
    x = ''.join(x)
    if x[0] != '0' and (x.count('0') + x.count('2') + x.count('4') + x.count('6')) == 2:
        print(x)
        ct += 1
print(ct)