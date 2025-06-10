def dels(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            if x % 2 != 0:
                dls.append(x)
            if (d // x) % 2 != 0:
                dls.append(d // x)
    return sorted(set(dls))
for x in range(18782, 18823):
    dls = dels(x)
    if len(dls) == 3:
        print(*dls)