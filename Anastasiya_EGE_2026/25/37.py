def dels(n):
    l = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            if x <= n // 2:
                l.append(x)
            if (n // x) <= n // 2:
                l.append(n // x)
    return sorted(set(l))


for y in range(1, 1_200_000):
    s = dels(y)
    if len(s) >= 3:
        s = s[-1] + s[-2] + s[-3]
        if s % 2022 == 0 and s != y:
            print(y, s)
