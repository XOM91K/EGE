import itertools
ct = 0
for x in itertools.product('0123456789AB', repeat = 8):
    x = ''.join(x)
    if x[0] != '0' and (x.count('3') + x.count('2') +x.count('5') +x.count('7') +x.count('B') > 2) and (int(x[0], 12) % 2 != int(x[1], 12) % 2):
        ct += 1
print(ct)