import itertools
ct = 0
for x in set(itertools.permutations('АВТОРОТА', 8)):
    x = ''.join(x)
    x = x.replace('Т', 'В')
    x = x.replace('Р', 'В')
    x = x.replace('О', 'А')
    if 'ВВ' not in x and 'АА' not in x:
        ct += 1
print(ct)