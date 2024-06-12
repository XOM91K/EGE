import itertools
for A in '02468':
    for x in range(0, 4):
        for B in itertools.product('13579', repeat=x):
            g = int('1' + A + '2157' + ''.join(B) + '4')
            if g % 133 == 0 and g <= 10 ** 10:
                print(g, g // 133)