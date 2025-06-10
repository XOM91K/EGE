def M(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    if len(dls) >= 2:
        return max(dls) + min(dls)
    else:
        return 0
ct = 0
for x in range(900_001, 10 ** 8):
    m = M(x)
    if str(m)[-2:] == '46':
        print(x, m)
        ct += 1
    if ct == 5:
        break