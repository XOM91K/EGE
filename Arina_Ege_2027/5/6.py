import itertools
ct = 0
for x in itertools.permutations('ВЕБИНАР', 7):
    x = ''.join(x)
    x = x.replace('Б', 'В')
    x = x.replace('Н', 'В')
    x = x.replace('Р', 'В')
    x = x.replace('И', 'Е')
    x = x.replace('А', 'Е')
    if 'ВВ' not in x and 'ЕЕ' not in x:
        ct += 1
print(ct)