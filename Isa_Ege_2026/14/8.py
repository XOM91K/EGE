def vn(d, n):
    s = []
    while d > 0:
        s.append(d % n)
        d //= n
    return s[::-1]
for n in range(2, 100):
    c = 39 * 15 ** 64 + 35 ** 450 + 74 * 43 ** 121 - 450035
    c = vn(c, n)
    print(n, c.count(8))
