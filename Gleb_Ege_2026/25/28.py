def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            if is_prime(x) and '3' in str(x) and '5' in str(x):
                dls.append(x)
            if is_prime(d // x) and '3' in str(d // x) and '5' in str(d // x):
                dls.append(d // x)
    return sorted(set(dls))
for x in range(4_000_001, 10 ** 7):
    dls = dels(x)
    if len(dls) == 2 and (dls[0] * dls[0] * dls[1] == x or dls[0] * dls[1] * dls[1] == x):
        print(x, max(dls))