import itertools
ct = 0
for x in set(itertools.permutations('АТТЕСТАТ')):
    x = ''.join(x)
    if 'АА' in x or 'АЕ' in x or 'ЕА' in x or 'ТТ' in x or 'ТС' in x or 'СТ' in x:
        ct += 1
print(ct)