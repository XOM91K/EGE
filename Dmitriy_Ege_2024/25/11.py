import itertools
tt = []
for A in '39':
    for x in range(0, 3):
        for B in itertools.product('02468', repeat=x):
            g = int('24' + ''.join(B) + '68' + A + '35')
            if g % 13 == 0 and g < 10 ** 9:
                tt.append([g, g // 13])
for x in sorted(tt):
    print(*x)