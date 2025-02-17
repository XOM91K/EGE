import itertools
ct = 0
for x in itertools.permutations('ВЕБИНАР'):
    x = ''.join(x)
    x = x.replace('Е', 'А')
    x = x.replace('И', 'А')
    x = x.replace('Б', 'В')
    x = x.replace('Н', 'В')
    x = x.replace('Р', 'В')
    if 'АА' not in x and 'ВВ' not in x:
        ct += 1
print(ct)