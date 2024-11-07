import itertools
ct = 0
for x in itertools.product('КРЕМНИЙ', repeat=5):
    x = ''.join(x)
    if x.count('Й') <= 2:
        x = x.replace('И', 'Е')
        if x.count('Е') % 2 == 0 and x.count('Е') > 1:
            ct += 1
print(ct)