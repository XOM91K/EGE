import itertools
ct = 0
for x in itertools.permutations('ХЛЕБНЫЙМЯКИШ', 7):
    x = ''.join(x)
    if x[0] == 'Х' and x[3] in 'БЫКИШ':
        x = x.replace('Б', '@')
        x = x.replace('Х', '@')
        x = x.replace('Л', '@')
        x = x.replace('Н', '@')
        x = x.replace('М', '@')
        x = x.replace('К', '@')
        x = x.replace('Ш', '@')
        x = x.replace('Й', '@')
        if '@@' not in x:
            ct += 1
print(ct)