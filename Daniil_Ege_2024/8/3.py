import itertools
g = 0
ct = 0
for x in itertools.product('БЖОУФЦЮ', repeat=4):
    x = ''.join(x)
    g += 1
    if g % 2 == 0 and x[0] == 'Ж' and x[1] == 'О':
        print(g , x)
        ct += 1
print(ct)
