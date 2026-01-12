def v11(n):
    s = []
    while n > 0:
        s.append(n % 11)
        n //= 11
    return s[::-1]
for x in range(1, 100000):
    if x % 3 == 0:
        d = v11(11 ** 250 + 11 ** 5 - 358123 - x)
        if d.count(10) == 248:
            print(x)