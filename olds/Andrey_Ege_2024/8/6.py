import itertools
ct = 0
for x in set(itertools.product('ВАСИЛИСА', repeat=6)):
    x = ''.join(x)
    if (x.count('А') + x.count('И')) > (x.count('В') + x.count('С') + x.count('Л')):
        ct += 1
print(ct)