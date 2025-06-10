import itertools
ct = 0
for x in itertools.permutations('ХЛЕБНЫЙМЯКИШ', 7):
    x = ''.join(x)
    if x[0] == 'Х' and x[3] in 'БЫКИШ':
        x = x.replace('Х', 'М')
        x = x.replace('Б', 'М')
        x = x.replace('К', 'М')
        x = x.replace('Ш', 'М')
        x = x.replace('Й', 'М')
        x = x.replace('Л', 'М')
        x = x.replace('Н', 'М')
        if 'ММ' not in x:
            ct += 1
print(ct)