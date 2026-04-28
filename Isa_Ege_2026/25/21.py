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
for x in range(5_700_001, 10 ** 7):
    dls = dels(x)
    if len(dls) > 0:
        M = dls[0] + dls[-1]
        if M > 70_000 and M ** 0.5 % 1 == 0:
            print(x, M)