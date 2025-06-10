import itertools
b = 0
for x in itertools.product(sorted('ЖЧГМЯФИ'), repeat=6):
    x = ''.join(x)
    b = b + 1
    if x[:2] == 'ЖЯ':
        print(b, x)
