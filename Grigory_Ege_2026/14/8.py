def vn(d, n):
    s = []
    while d > 0:
        s.append(d % n)
        d //= n
    return s[::-1]

for i in range(10, 36):
    a = 39 * 15 ** 64 + 35 ** 450 + 74 * 43 ** 121 - 450035
    a = vn(a, i)
    print(i, a.count(8))