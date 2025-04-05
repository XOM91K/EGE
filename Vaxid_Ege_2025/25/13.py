def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    return sorted(set(dls))
for x in range(112_500_000, 112_550_001):
    dls = dels(x)
    M = 0
    if len(dls) >= 2:
        M = dls[-1] + dls[-2]
        if str(M)[-4:] == '1214':
            print(x)