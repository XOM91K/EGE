import itertools
z = 0
for x in itertools.product('ЕКМОПРТЬЮ', repeat=5):
    x = ''.join(x)
    z += 1
    if z % 2 != 0 and x[0] != 'Ь' and x.count('К') == 2:
        print(z, x)
