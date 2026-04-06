def dels(d):
    l = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            if x % 100 == 11 and x != 11:
                l.append(x)
            if (d // x) % 100 == 11 and (d // x) != 11:
                l.append(d // x)
    return sorted(set(l))


for x in range(1350051, 10 ** 9):
    l = dels(x)
    if len(l) > 0:
        print(x, min(l))
