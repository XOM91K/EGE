import itertools
ct = 0
for x in itertools.product('КРЕМНИЙ', repeat=5):
    x = ''.join(x)
    if (x.count('Е') + x.count('И')) % 2 == 0:
        if 'Е' in x or 'И' in x:
            if x.count('Й') <= 2:
                ct += 1
print(ct)