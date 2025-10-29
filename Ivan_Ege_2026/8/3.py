import itertools
ct = 0
for x in itertools.permutations('ВЕБИНАР', 7):
    x = ''.join(x)
    x = x.replace('Б', 'В')
    x = x.replace('Н', 'В')
    x = x.replace('Р', 'В')
    x = x.replace('А', 'И')
    x = x.replace('Е', 'И')
    if 'ВВ' not in x and 'ИИ' not in x:
        ct += 1
print(ct)