import itertools
ct = 0
for x in itertools.product('0123456789ab', repeat=3):
    x = ''.join(x)
    if x[0] != '0' and x.count('2') == 1:
        if x[0] != x[1] and x[1] != x[2]:
            ct += 1
print(ct)