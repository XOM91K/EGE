import itertools
ct = 0
for x in itertools.permutations('КОМЕТА', 6):
    x = ''.join(x)
    x = x.replace('О', 'Е')
    x = x.replace('А', 'Е')
    x = x.replace('М', 'К')
    x = x.replace('Т', 'К')
    if 'ЕЕ' not in x and 'КК' not in x:
        ct += 1
print(ct)