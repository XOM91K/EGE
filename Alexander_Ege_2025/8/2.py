import itertools
ct = 0
for x in itertools.product('СЛОН', repeat=5):
    x = ''.join(x)
    if x.count('С') == 1:
        ct += 1
print(ct)