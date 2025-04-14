import itertools
ct = 0
for x in itertools.permutations('ХЛЕБНЫЙМЯКИШ',7):
    x=''.join(x)
    if x[0] == "Х":
        if x[3] in 'БЫКИШ':
            x = x.replace('Х', 'Л')
            x = x.replace('Б', 'Л')
            x = x.replace('Н', 'Л')
            x = x.replace('Й', 'Л')
            x = x.replace('М', 'Л')
            x = x.replace('К', 'Л')
            x = x.replace('Ш', 'Л')
            if 'ЛЛ' not in x:
                ct += 1
print(ct)