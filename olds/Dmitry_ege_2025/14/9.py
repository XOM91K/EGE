def vx(d, x):
    s = []
    while d > 0:
        s.append(d % x)
        d //= x
    return s[::-1]
d = 39 * 15 ** 64 + 35 ** 450 + 74 * 43 ** 121 - 450035
for x in range(9, 1000):
    f = vx(d, x)
    print(x, f.count(8))