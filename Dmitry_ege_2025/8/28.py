import itertools
ct = 0
for x in itertools.product(sorted('КРЕМНИЙ'), repeat=5):
    x = ''.join(x)
    if (x.count('Е') + x.count('И')) > 0 and (x.count('Е') + x.count('И')) % 2 == 0 and x.count('Й') <= 2:
        ct += 1
print(ct)