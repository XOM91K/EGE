def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    l = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            if is_prime(x):
                l.append(x)
            if is_prime(d // x):
                l.append(d // x)
    return sorted(set(l))
for x in range(1_475_000, 1, -1):
    l = dels(x)
    S = sum(l)
    if S != 0 and S <= 42000 and S % 6 == 0:
        print(x, S)