def v15(d):
    s = []
    while d > 0:
        s.append(d % 15)
        d //= 15
    return s[::-1]


g = 3 * 15 ** 1140 + 2 * 15 ** 1025 + 15 ** 923 - 3 * 15 ** 85 + 2 * 15 ** 74 + 3
g = v15(g)
g = ' '.join([str(d) for d in g])
for x in range(1000):
    if '0 ' * x in g:
        print('0:', x)
    if '14 ' * x in g:
        print('14:', x)