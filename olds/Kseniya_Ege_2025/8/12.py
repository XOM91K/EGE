import itertools
ct = 0
for x in itertools.permutations('ВЕБИНАР', 7):
    x = ''.join(x)
    x = x.replace('Е', 'А')
    x = x.replace('И', 'А')
    x = x.replace('В', 'Б')
    x = x.replace('Н', 'Б')
    x = x.replace('Р', 'Б')
    if 'АА' not in x and 'ББ' not in x:
        ct += 1
print(ct)