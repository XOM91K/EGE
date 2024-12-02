import itertools
ct = 0
for x in set(itertools.product('СВЕТЛАНА', repeat=8)):
    x = ''.join(x)
    if x.count('С') == 1 and x.count('В') == 1 and x.count('Е') == 1 and x.count('Т') == 1 and x.count('Л') == 1 and x.count('Н') == 1 and x.count('А') == 2 and 'АА' not in x:
        ct += 1
print(ct)