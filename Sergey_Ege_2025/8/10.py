import itertools

ct = 0
for x in set(itertools.permutations('МСТИЛАВ', 5)):
    x = ''.join(x)
    if x.count('М') + x.count('С') + x.count('Т') + x.count('Л') + x.count('В') > x.count('И') + x.count('А'):
        if 'АА' not in x and 'АИ' not in x and 'ИА' not in x and 'ИИ' not in x:
           print(x)

           ct += 1
print(ct)
