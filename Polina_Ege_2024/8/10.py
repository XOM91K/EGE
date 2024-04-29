import itertools
ct = 0
for x in set(itertools.product('ГИПЕРБОЛА', repeat=6)):
    x = ''.join(x)
    if x[0] not in 'ИЕОА' and x[-1] not in 'ИЕОА':
        x = x.replace('П', 'Г')
        x = x.replace('Р', 'Г')
        x = x.replace('Б', 'Г')
        x = x.replace('Л', 'Г')
        x = x.replace('И', 'А')
        x = x.replace('Е', 'А')
        x = x.replace('О', 'А')
        if 'ГАГ' not in x:
            ct += 1
print(ct)