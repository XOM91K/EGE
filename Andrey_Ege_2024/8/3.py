import itertools
k = 0
for x in itertools.product('ЕКМОПРТЬЮ', repeat=5):
    x = ''.join(x)
    k += 1
    if k % 2 != 0 and x[0] != 'Ь' and x.count('К') == 2:
        print(k)