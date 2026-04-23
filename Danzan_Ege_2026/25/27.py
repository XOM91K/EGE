def is_prime(d):
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if is_prime(x) and x % 2 != 0:
                l.append(x)
            if is_prime(d//x) and (d//x) % 2 != 0:
                l.append(d//x)
    return sorted(set(l))
for x in range(5_000_001, 10_000_000):
    d = dels(x)
    if len(d) == 2 and x == (d[0] * d[1]) and is_prime(abs(d[0] - d[1])):
        print(x, max(d))