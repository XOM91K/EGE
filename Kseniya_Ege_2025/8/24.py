import itertools
ct= 0
for x in itertools.permutations('ГЛУБИНА'):
    x = ''.join(x)
    if x.index('Г') > x.index('А') and x.index('Г') > x.index('И'):
        ct += 1
print(ct)
# d = 'ГЛУБИНА'
# print(d.index('У'))
# print(d.index('Н'))