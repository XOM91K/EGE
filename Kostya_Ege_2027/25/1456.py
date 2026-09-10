def dels(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            if is_prime(x):
                dls.append(x)
            if is_prime(d // x):
                dls.append(d // x)
    return sorted(set(dls))
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
for x in range(1_200_001, 10**8):
    dls = (dels(x))
    if len(dls) > 0:
        M = min(dls) + max(dls)
        if M > 2000 and str(M)[-1] == '8':
             print(x,M)