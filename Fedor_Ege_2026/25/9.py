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
for x in range(1_324_999, 1, -1):
    S = sum(dels(x))
    if S != 0 and S <= 30_000 and S % 5 == 0:
        print(x)
