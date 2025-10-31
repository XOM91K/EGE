def dels(d):
    l = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            if x % 2 != 0:
                l.append(x)
            if (d // x) % 2 != 0:
                l.append(d // x)
    return l
for x in range(18782, 18823):
    nch = dels(x)
    if len(nch) == 3:
        print(*sorted(nch))