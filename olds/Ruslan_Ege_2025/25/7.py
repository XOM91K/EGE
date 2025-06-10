def M(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    dls = sorted(set(dls))
    if len(dls) >= 2:
        return dls[-1] + dls[0]
    else:
        return 0
ct = 0
for y in range(900_001, 10 ** 10):
    g = M(y)
    if g % 100 == 46:
        print(y, g)
        ct += 1
    if ct == 5:
        break