def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    return sorted(set(dls))
for x in range(500_001, 10 ** 10):
    R = sum(dels(x))
    if str(R)[-1] == '6':
        print(x, R)