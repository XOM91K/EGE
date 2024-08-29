import itertools
ct = 0
for x in itertools.permutations("ГЛУБИНА"):
    x = ''.join(x)
    if x.index('Г') > x.index('И') and x.index('Г') > x.index('А'):
        print(x)
        ct += 1
print(ct)