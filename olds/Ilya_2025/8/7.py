import itertools
ct = 0
for x in itertools.product(set('ЕСТЕСТВО'), repeat=8):
    x = ''.join(x)
    x = x.replace('О', 'Е')
    x = x.replace('С', 'В')
    x = x.replace('Т', 'В')
    if x.count('Е') >= 3 and x.count('В') >= 4:
        if 'ЕЕ' not in x:
            ct += 1
print(ct)