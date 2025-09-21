import itertools
ct=  0
for x in itertools.permutations('ГЛУБИНА', 7):
    x = ''.join(x)
    if x.index('Г') > x.index('А') and x.index('Г') > x.index('И'):
        print(x)
        ct += 1
print(ct)