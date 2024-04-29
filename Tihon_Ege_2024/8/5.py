import itertools
ct = 0
for x in set(itertools.permutations('АББАТИСА')):
    x = ''.join(x)
    x = x.replace('И', 'А')
    x = x.replace('Т', 'Б')
    x = x.replace('С', 'Б')
    if 'ББ' not in x and 'АА' not in x:
        ct += 1
print(ct)