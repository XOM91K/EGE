def vp(n, p):
    s = []
    while n > 0:
        s.append(n % p)
        n //= p
    return s[::-1]
for x in range(2, 20):
    d = 39 * 15 ** 64 + 35 ** 450 + 74 * 43 ** 121 - 450035
    d = vp(d, x)
    print(x, d.count(8))