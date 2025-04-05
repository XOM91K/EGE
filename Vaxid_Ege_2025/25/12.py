def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    return dls
ct = 0
for x in range(500_001, 10 ** 10):
    dls = dels(x)
    M = 0
    if len(dls) > 0:
        M = sum(dls)
        if str(M)[-1] == '9':
            print(x, M)
            ct = ct + 1
        if ct == 5:
            break