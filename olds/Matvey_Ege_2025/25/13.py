def dels(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    return sorted(set(dls))
for x in range(700_001, 10 ** 10):
    M = dels(x)
    if len(M) >= 1:
        M = M[0] + M[-1]
    else:
        M = 0
    if str(M)[-1] == '4':
        print(x, M)