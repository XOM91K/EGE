import itertools
ct = 0
for x in itertools.permutations('ГЛУБИНА', 7):
    x = ''.join(x)
    A = x.index('А')
    I = x.index('И')
    mx = max(A, I)
    if x.index('Г') > mx:
        ct = ct + 1
        print(ct)