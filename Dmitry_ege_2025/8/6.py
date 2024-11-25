import itertools
ct = 0
for x in itertools.product('ИГОРЬ', repeat=8):
    x = ''.join(x)
    if x.count('О') == 1 and x.count('Ь') == 1:
        if x[0] != 'Ь':
            ct += 1
print(ct)