import itertools
ct = 0
for x in itertools.permutations('ВЕБИНАР', 7):
    x = ''.join(x)
    x = x.replace('Р', 'Б')
    x = x.replace('В', 'Б')
    x = x.replace('Н', 'Б')
    x = x.replace('И', 'А')
    x = x.replace('Е', 'А')
    if 'ББ' not in x and 'АА' not in x:
        ct = ct + 1
print(ct)