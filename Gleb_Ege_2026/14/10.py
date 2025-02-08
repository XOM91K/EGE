def vx(f, x):
    s = []
    while f > 0:
        s.append(f % x)
        f //= x
    return s[::-1]
d = 39 * 15 ** 64 + 35 ** 450 + 74 * 43 ** 121 - 450035
for x in range(9, 100):
    f = vx(d, x)
    print(f.count(8), x)