import itertools
ct = 0
for x in itertools.permutations('КОМПЬЮТЕР'):
    x = ''.join(x)
    if x[-2] == 'Е' and sorted(x[:4]) == list(x[:4]):
        ct += 1
print(ct)