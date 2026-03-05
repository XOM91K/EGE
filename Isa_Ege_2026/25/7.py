def dels(d):
    l = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return sorted(set(l))
for x in range(700_001, 10 ** 7):
    dls = dels(x)
    if len(dls) > 0:
        M = max(dls) + min(dls)
        if str(M)[-1] == '4':
            print(x, M)