import itertools
ct = 0
for x in set(itertools.product('галактика', repeat=8)):
    x = ''.join(x)
    if x[0] in 'гклт' and 'кл' not in x and x[-1] in 'аи':
        ct += 1
print(ct)