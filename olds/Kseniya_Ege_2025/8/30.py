import itertools
ct = 0
k = 0
for x in itertools.product('ЕЛОПРСТ', repeat=5):
    x = ''.join(x)
    k += 1
    if x[-1] in 'ЕО' and k % 2 != 0:
        if x.count('Л') + x.count('П') + x.count('Р') + x.count('С') + x.count('Т') <= 3:
            ct += 1
print(ct)