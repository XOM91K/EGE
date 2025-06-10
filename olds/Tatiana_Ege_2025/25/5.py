def M(d):
    dl = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            dl.append(x)
            dl.append(d // x)
    dl = sorted(set(dl))
    if len(dl) >= 2:
        return dl[0] + dl[-1]
    else:
        return 0
ct = 0
for x in range(900_001, 10 ** 8):
    g = M(x)
    if str(g)[-2:] == '46':
        ct += 1
        print(x, g)
    if ct == 5:
        break