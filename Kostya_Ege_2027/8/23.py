import itertools
ct = 0
for x in itertools.permutations('ТИХОРЕЦК', 4):
    x = ''.join(x)
    k = 0
    #if len(set(x)) == 4:
    c = 'ТИХО'
    for z in range(0, 4):
        if x[z] == c[z]:
            k += 1
    if k == 2:
        x = x.replace('О', 'И')
        x = x.replace('Е', 'И')
        if x.count('И') == 2:
            ct += 1


print(ct)