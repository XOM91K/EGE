def dels(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            if x % 2 != 0:
                dls.append(x)
            if (d // x) % 2 != 0:
                dls.append(d // x)
    return sorted(set(dls))
for t in range(18782, 18823):
    g = dels(t)
    if len(g) == 3:
        print(g[0], g[1], g[2])