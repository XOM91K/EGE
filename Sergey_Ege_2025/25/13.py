def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if is_prime(x):
                dls.append(x)
            if is_prime(d // x):
                dls.append(d // x)
    dls = sorted(dls)
    return dls


def is_prime(d):
    if d == 1:
        return False
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return True

ct = 0
for x in range(1000001,10**9):
    d = dels(x)
    if len(d) == 3:
        print(x, d[-1])
        ct += 1
    if ct == 5:
        break