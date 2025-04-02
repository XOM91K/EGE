def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            if is_prime(x):
                dls.append(x)
            if is_prime(n // x):
                dls.append(n // x)
    return sorted(set(dls))
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
for x in range(33_333, 55_555):
    dls = dels(x)
    if len(dls) > 0 and x % sum(dls) == 0 and sum(dls) > 250:
        print(x, sum(dls))
