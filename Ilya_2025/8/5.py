import itertools
ct = 0
for x in itertools.permutations('ГЕРАСИМ'):
    x = ''.join(x)
    x = x.replace('А', 'Е')
    x = x.replace('И', 'Е')
    x = x.replace('Р', 'Г')
    x = x.replace('С', 'Г')
    x = x.replace('М', 'Г')
    if 'ГГ' not in x and 'ЕЕ' not in x:
        print(x)
        ct += 1
print(ct)