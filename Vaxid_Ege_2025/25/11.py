def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    return sorted(set(dls))
for x in range(700_000, 2, -1):
    M = dels(x)
    if len(M) > 0:
        M = sum(M) // len(M)
        if str(M)[-3:] == '313':
            print(x, M)