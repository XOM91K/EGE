import itertools
ct = 0
for x in itertools.product('ЕКМОПРТЬЮ', repeat = 5):
    x = ''.join(x)
    ct += 1
    if x[0] != 'Ь' and x.count('К') == 2:
        if ct % 2 != 0:
            print (ct)