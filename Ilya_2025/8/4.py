import itertools
ct = 0
for x in itertools.product('ПОЛИНА', repeat=8):
    x = ''.join(x)
    sg = gl = 0
    x = x.replace('Л', 'Н')
    x = x.replace('П', 'Н')
    x = x.replace('И', 'О')
    x = x.replace('А', 'О')
    if x.count('Н') > x.count('О'):
        ct += 1
print(ct)