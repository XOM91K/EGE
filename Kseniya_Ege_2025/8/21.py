import itertools
ct = 0
n = 0
for x in itertools.product('ЕЛОПРСТ', repeat=5):
    x = ''.join(x)
    n += 1
    if n % 2 == 1 and (x[-1] in 'ЕО'):
        if x.count('Л') + x.count('П') + x.count('Р') + x.count('Т') + x.count('С') <= 3:
            print(x)
            ct += 1
print(ct)