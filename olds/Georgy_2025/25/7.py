def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    dls = sorted(set(dls))
    if len(dls) > 0:
        return dls[0] + dls[-1]
    else:
        return 0
for x in range(700001, 10 ** 10):
    M = dels(x)
    if str(M)[-1] == '4':
        print(x, M)