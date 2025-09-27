import itertools
ct=0
for x in itertools.permutations('хлебныймякиш',7):
    x=''.join(x)
    if x[0]=='х':
        if x[3] in 'быкиш':
            x=x.replace('л','х').replace('б','х').replace('н','х').replace('й','х').replace('м','х').replace('к','х').replace('ш','х')
            if 'хх' not in x:
                ct+=1
print(ct)