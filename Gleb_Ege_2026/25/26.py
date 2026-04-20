ct = 0
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def f(n):
    l = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            if is_prime(x):
                l.append(x)
            if is_prime(n // x):
                l.append(n // x)
    return sorted(set(l))
for x in range(7_800_001, 8_000_000):
    a = f(x)
    if len(a) > 0:
        M = a[0] + a[-1]
        if str(M)[-2:] == '63' and M % len(a) == 0:
            print(x, M)
            ct += 1
            if ct == 5:
                break