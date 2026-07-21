import itertools
ct = 0
tmb = 'ВОЛК'
for x in itertools.product('ПОЛЯКВ',repeat=4):
    x = ''.join(x)
    k = 0
    for y in range(len(tmb)):
        if tmb[y] == x[y]:
            k += 1
    if k == 2:
        ct += 1
        print(x)
print(ct)