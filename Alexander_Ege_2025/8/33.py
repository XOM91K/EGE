import itertools
ct = 0
for x in itertools.permutations('ХЛЕБНЫЙМЯКИШ', 7):
    x = ''.join(x)
    if x[0] == 'Х' and x[3] in 'БЫКИШ':
        x = x.replace('Л', 'Х')
        x = x.replace('Б', 'Х')
        x = x.replace('Н', 'Х')
        x = x.replace('Й', 'Х')
        x = x.replace('М', 'Х')
        x = x.replace('К', 'Х')
        x = x.replace('Ш', 'Х')
        if 'ХХ' not in x:
            ct += 1
print(ct)