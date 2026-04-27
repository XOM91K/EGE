import itertools
ct = 0
for x in itertools.product('ДЕВИАЦЯ', repeat=8):
    x = ''.join(x)
    if x[0] in 'ИАЕЯ' and x[-1] in 'ДВЦ':
        if 'ДЕ' in x:
            ct += 1
print(ct)