def vn(d, n):
    s = []
    while d > 0:
        s.append(d % n)
        d //= n
    return s[::-1]
for n in range(9, 100):
    d = 39 * 15 ** 64 + 35 ** 450 + 74 * 43 ** 121 - 450035
    d = vn(d, n)
    print(n, d.count(8))