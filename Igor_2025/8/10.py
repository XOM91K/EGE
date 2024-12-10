import itertools
i = 0
ct = 0
for x in itertools.product(sorted('ПРЕСТОЛ'), repeat=5):
    x = ''.join(x)
    i += 1
    if i % 2 != 0 and x[-1] in 'ЕО' and (x.count('П') + x.count('Р') + x.count('С') + x.count('Т') + x.count('Л')) <= 3:
        ct += 1
print(ct)
