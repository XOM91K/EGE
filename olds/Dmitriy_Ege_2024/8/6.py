import itertools
ct = 0
for x in set(itertools.permutations('КОМПЬЮТЕР')):
    x = ''.join(x)
    if list(x[:4]) == sorted(x[:4]) and x[-2] == 'Е':
        ct += 1
print(ct)