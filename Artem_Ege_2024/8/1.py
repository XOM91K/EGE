import itertools
ct = 0
for x in itertools.product('ЕГЭ', repeat=5):
    x = ''.join(x)
    if x[0] in 'ЕЭ':
        print(x)
        ct += 1
print(ct)