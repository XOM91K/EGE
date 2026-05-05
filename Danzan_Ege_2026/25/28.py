def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if is_prime(x) and (str(x).count('4') >= 1 or str(x).count('7') >= 1):
                l.append(x)
            if is_prime(d//x) and (str(d//x).count('4') >= 1 or str(d//x).count('7') >= 1):
                l.append(d//x)
    return sorted(set(l))
for x in range(2_400_001, 10_000_000):
    l = dels(x)
    if len(l) == 3 and l[0] * l[1] * l[2] == x:
        print(x, max(l))