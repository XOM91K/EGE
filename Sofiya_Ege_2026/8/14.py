import itertools
ct=0
for x in itertools.permutations('левиоса', 7):
    x=''.join(x)
    if x[0] not in 'еиоа':
        if x[3] not in 'лвс':
            ct+=1
print(ct)