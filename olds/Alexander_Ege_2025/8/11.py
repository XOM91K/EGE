import itertools
ct = 0
for x in itertools.permutations('ВЕБИНАР', 7):
    x = ''.join(x)
    x = x.replace('А', 'Е')
    x = x.replace('И', 'Е')
    x = x.replace('Б', 'В')
    x = x.replace('Н', 'В')
    x = x.replace('Р', 'В')
    if 'ЕЕ' not in x and 'ВВ' not in x:
        ct += 1
print(ct)