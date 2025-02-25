import itertools
ct = 0
for x in set(itertools.product('ДЕВИАЦИЯ', repeat = 8)):
    x = ''.join(x)
    if x[0] in 'ЕИАЯ' and x[-1] in 'ДВЦ' and 'ДЕ' in x:
        ct += 1
print(ct)