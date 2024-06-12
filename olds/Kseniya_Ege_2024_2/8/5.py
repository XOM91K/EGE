import itertools
ct = 0
ct2 = 0
for x in set(itertools.permutations('АТТЕСТАТ', 8)):
    x = ''.join(x)
    if 'АА' in x or 'СС' in x or 'ТТ' in x or 'АЕ' in x or 'ЕА' in x or 'СТ' in x or 'ТС' in x:
        ct += 1
print(ct, ct2)