import itertools
ct = 0
for x in itertools.product('КРЕМНИЙ', repeat=5):
    x = ''.join(x)
    if x.count('Й') <= 2 and ('Е' in x or 'И' in x) and (x.count('Е') + x.count('И')) % 2 == 0:
        ct += 1
print(ct)