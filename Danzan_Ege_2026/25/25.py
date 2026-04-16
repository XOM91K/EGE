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
                l.append(d//x)
    return sorted(set(l))

for x in range(5_700_001, 10_000_000):
    d = dels(x)
    if len(d) > 1:
        M = max(d) + min(d)
        if M > 70_000 and M**0.5 == int(M**0.5):
            print(x, M)