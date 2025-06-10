def M(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    dls = sorted(set(dls))
    if len(dls) > 0:
        M2 = dls[0] + dls[-1]
        return M2
    else:
        return 0
for x in range(900_001, 10 ** 10):
    MM = M(x)
    if str(MM)[-2:] == '46':
        print(x, MM)