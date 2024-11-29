import itertools
ct = 0
for x in itertools.permutations('ВЕБИНАР', 7):
    x = ''.join(x)
    x = x.replace('Е', 'А')
    x = x.replace('И', 'А')
    x = x.replace('Б', 'В')
    x = x.replace('Н', 'В')
    x = x.replace('Р', 'В')
    if 'ВВ' not in x and 'АА' not in x:
        ct += 1
print(ct)