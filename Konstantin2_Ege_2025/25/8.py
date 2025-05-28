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
for x in range(1_200_001, 10 ** 10):
    if len(dels(x)) >= 1:
        M = min(dels(x)) + max(dels(x))
        if M > 2000 and str(M)[-1] == '8':
            print(x, M)