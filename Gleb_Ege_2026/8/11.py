import itertools
ct = 0
for x in itertools.product(sorted('КРЕМНИЙ'), repeat=5):
    x = ''.join(x)
    x = x.replace('Е', '1')
    x = x.replace('И', '1')
    if '1' in x and x.count('1') % 2 == 0 and x.count('Й') <= 2:
        ct += 1
print(ct)
