def dels(d):
    dl = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            if x % 2 != 0:
                dl.append(x)
            if (d // x) % 2 != 0:
                dl.append(d // x)
    return sorted(set(dl))
for x in range(18782, 18823):
    g = dels(x)
    if len(g) == 3:
        print(*g)