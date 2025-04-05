import itertools
ct = 0
for x in itertools.permutations('ХЛЕБНЫЙМЯКИШ', 7):
    x = ''.join(x)
    if x[0] == 'Х' and x[3] in 'БЫКИШ':
        x = x.replace('Х', '1')
        x = x.replace('Л', '1')
        x = x.replace('Б', '1')
        x = x.replace('Н', '1')
        x = x.replace('Й', '1')
        x = x.replace('М', '1')
        x = x.replace('К', '1')
        x = x.replace('Ш', '1')
        if '11' not in x:
            ct += 1
print(ct)