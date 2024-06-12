import itertools
ct = 0
for x in itertools.product('БАНДЕРОЛЬ', repeat=7):
    x = ''.join(x)
    if x.count('Ь') <= 1:
        x = x.replace('Н', 'Б')
        x = x.replace('Д', 'Б')
        x = x.replace('Р', 'Б')
        x = x.replace('Л', 'Б')
        if 'БЕ' not in x and 'ЕБ' not in x:
            ct += 1
print(ct)