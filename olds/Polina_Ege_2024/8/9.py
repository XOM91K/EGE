import itertools
ct = 0
for x in itertools.product('ГИПЕРБОЛА', repeat=6):
    x = ''.join(x)
    x = x.replace('Е', 'И')
    x = x.replace('О', 'И')
    x = x.replace('А', 'И')
    x = x.replace('П', 'Г')
    x = x.replace('Р', 'Г')
    x = x.replace('Б', 'Г')
    x = x.replace('Л', 'Г')
    if x[0] != 'И' and x[-1] != 'И':
        if 'ГИГ' not in x:
            ct += 1
print(ct)