def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    return sorted(set(dls))
n = 100
print(dels(n))