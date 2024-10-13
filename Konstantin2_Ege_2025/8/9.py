import itertools
ct = 0
for x in itertools.permutations('ВЕБИНАР', 7):
    x = ''.join(x)
    x = x.replace('Б', 'В').replace('Н', 'В').replace('Р', 'В')
    x = x.replace('И', 'Е').replace('А', 'Е')
    if 'ЕЕ' not in x and 'ВВ' not in x:
        ct += 1
print(ct)