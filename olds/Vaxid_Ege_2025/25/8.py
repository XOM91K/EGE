def dels(n):
    dls = []
    for x in range(1, n + 1):
        if n % x == 0:
            dls.append(x)
    return dls
ct = 0
for x in range(800_001, 10 ** 10):
    dls = dels(x)
    M = 0
    if len(dls) > 2:
        M = dls[1] + dls[-2]
    if str(M)[-1] == '4':
        print(x, M)
        ct += 1
    if ct == 5:
        break