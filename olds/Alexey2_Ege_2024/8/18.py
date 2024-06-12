import itertools
ct = 0
for x in itertools.product('БАНДЕРОЛЬ', repeat = 7):
    x = ''.join(x)
    if x.count('Ь') <= 1:
        x = x.replace('Н', 'Б')
        x = x.replace('Д', 'Б')
        x = x.replace('Р', 'Б')
        x = x.replace('Л', 'Б')
        if 'ЕБ' not in x and 'БЕ' not in x:
            ct += 1
print(ct)