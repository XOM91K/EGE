import itertools
ct = 0
for x in set(itertools.permutations('ПРЕПАРАТ', 8)):
    x = ''.join(x)
    if ('АЕ' in x or 'ЕА' in x or 'АА' in x ) or ('ПП' in x or 'ПР' in x or 'РП' in x or 'ПТ' in x or 'ТП' in x or 'ТТ' in x or 'РР' in x or 'ТР' in x or 'РТ' in x):
        ct += 1
print(ct)