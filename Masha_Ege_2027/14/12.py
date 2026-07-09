def vn(d, p):
    s = []
    while d > 0:
        s.append(d % p)
        d //= p
    return s[::-1]
for x in range(9, 100):
    c = 39 * 15 ** 64 + 35 ** 450 + 74 * 43 ** 121 - 450035
    d = vn(c, x)
    print(x, d.count(8))