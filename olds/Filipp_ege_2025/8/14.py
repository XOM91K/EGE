import itertools
k = 0
ct = 0
for x in itertools.product(sorted('ПРЕСТОЛ'), repeat=5):
    x=  ''.join(x)
    k += 1
    if k % 2 == 1 and x[-1] in 'ОЕ':
        if x.count('П') + x.count('Р') + x.count('С') + x.count('Т') + x.count('Л') <= 3:
            ct += 1
print(ct)