def dels(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    dls = sorted(set(dls))
    return dls
ct = 0
for x in range(700000, 1, -1):
    dls = dels(x)
    if len(dls) > 0:
        M = sum(dls) // len(dls)
        if str(M)[-3:] == '313':
            print(x, M)
            ct += 1
            if ct == 7:
                break