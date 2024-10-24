import itertools
n = 0
for x in itertools.product('опстуцшю', repeat=6):
    x = ''.join(x)
    n = n + 1
    if x[0] == 'ю' and x[1] == 'ш' and x[2] == 'о' and x[3] == 'с'  and x[4] == 'с' and x[5] == 'о':
        print(n, x)