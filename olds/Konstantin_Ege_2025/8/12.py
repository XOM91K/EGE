import itertools
ct = 0
for x in itertools.product('0123', repeat=4):
    x = ''.join(x)
    if x[0] != '0' and (x.count('0') >= 2 or x.count('1') >= 2 or x.count('2') >= 2 or x.count('3') >= 2):
        ct += 1
        print(x)
print(ct)