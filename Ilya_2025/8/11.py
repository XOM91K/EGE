import itertools
ct = 0
k = 0
for x in itertools.permutations('МУЖЧИНА', 6):
    x = ''.join(x)
    k += 1
    if x[0] != 'Ч' and 'Ж' in x:
        ct += 1
        print(k, x)
print(ct // 2)