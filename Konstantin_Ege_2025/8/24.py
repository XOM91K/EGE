import itertools
ct = 0
for x in itertools.product('0123456789ab', repeat=5):
    x = ''.join(x)
    if x[0] != '0' and x.count('7') == 1 and (x.count('9') + x.count('a') + x.count('b')) <= 3:
        ct += 1
print(ct)