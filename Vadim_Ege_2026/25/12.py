def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if x % 2 == 0:
                l.append(x)
            if (d // x) % 2 == 0:
                l.append(d // x)
    return sorted(set(l))
for x in range(95_632, 95_701):
    d = dels(x)
    if len(d) == 6:
        print(*d)