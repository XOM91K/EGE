import itertools
ct = 0
for x in itertools.product('ШКОЛА', repeat=5):
    x = ''.join(x)
    if 'О' in x or 'А' in x:
        print(x)
        ct += 1
print(ct)