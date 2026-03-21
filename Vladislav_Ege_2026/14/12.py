def vn(d, n):
    s = []
    while n > 0:
        s.append(n % d)
        n //= d
    return s[::-1]
for x in range(9, 100):
    dd = 39 * 15 ** 64 + 35 ** 450 + 74 * 43 ** 121 - 450035
    dd = vn(x, dd)
    print(dd.count(8))