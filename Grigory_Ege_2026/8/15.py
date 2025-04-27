import itertools
ct = 0
for x in itertools.product('ДЕВИАЦЯ',repeat=8):
    x = ''.join(x)
    if x[0] in 'ЕИАЯ' and 'ДЕ' in x and x[-1] in 'ДВЦ':
        ct += 1
print(ct)