import itertools
ct = 0
for x in itertools.permutations('ГЛУБИНА'):
    x = ''.join(x)
    if x.index('Г') > x.index('А') and x.index('Г') > x.index('И'):
        ct += 1
print(ct)
# s = 'СОБАЧКА'
# print(s.index('Б'))