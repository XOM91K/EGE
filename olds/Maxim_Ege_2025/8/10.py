import itertools
ct = 0
for x in itertools.permutations('АБВЕИНР'):
    x = ''.join(x)
    if 'АА' not in x and 'АЕ' not in x and 'АИ' not in x and 'ЕА' not in x and 'ЕЕ' not in x and 'ЕИ' not in x and 'ИА' not in x and 'ИЕ' not in x and 'ИИ' not in x and 'ББ' not in x and 'БВ' not in x and 'БН' not in x and 'БР' not in x and 'ВБ' not in x and 'ВВ' not in x and 'ВН' not in x and 'ВР' not in x and 'НБ' not in x and 'НВ' not in x and 'НН' not in x and 'НР' not in x and 'РБ' not in x and 'РВ' not in x and 'РН' not in x and 'РР' not in x:
        ct += 1
        print(ct,x)