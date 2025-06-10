def dels(n):
    dls = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    dls = sorted(set(dls))
    M = dls[1] + dls[-2]
    return M
for x in range(800_000, 10 ** 10):
    M = dels(x)
    if str(M)[-1] == '4':
        print(x, M)