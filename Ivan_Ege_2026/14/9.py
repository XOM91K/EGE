mx = []
for x in range(20000):
    a = x**2 + 17*x + 53
    c = 0
    while a > 0:
        if a%38 == 10:
            c += 1
        a //= 38
    mx.append([c, x])
print(sorted(mx, key = lambda x: (-x[0], -x[1]))[:3])
print(10024 ** 2 + 17 * 10024 + 53)