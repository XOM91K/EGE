def is_prime(d):
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if is_prime(x) and '5' in str(x) and '3' in str(x):
                l.append(x)
            if is_prime(d//x) and '5' in str(d//x) and '3' in str(d//x):
                l.append(d//x)
    return sorted(l)
for x in range(4_000_001, 10_000_000):
    d = dels(x)
    if (len(d) == 2 and x == (d[0] * d[1] * d[0])) or (len(d) == 2 and x == (d[1] * d[1] * d[0])):
        print(x, max(d))