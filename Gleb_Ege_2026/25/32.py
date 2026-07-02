def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            if is_prime(x):
                dls.append(x)
            if is_prime(d // x):
                dls.append(d // x)
    return sorted(set(dls))
for x in range(8_117_600_757, 10 ** 10):
    dls = dels(x)
    if len(dls) >= 2:
        M = dls[-1] - dls[0]
        if is_prime(M) and str(M).count('1') >= 4:
            print(x, M)