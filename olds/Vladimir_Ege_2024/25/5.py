def dels(n):
    l = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            if x % 2 != 0:
                l.append(x)
            if (n // x) % 2 != 0:
                l.append(n // x)
    return sorted(set(l))
for x in range(190061, 190073):
    d = dels(x)
    if len(d) == 4:
        print(d[-1], d[-2])