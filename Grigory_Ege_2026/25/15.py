def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if is_prime(x) and str(x).count('3') == 2:
                l.append(x)
            if is_prime(d // x) and str(d // x).count('3') == 2:
                l.append(d // x)
    return sorted(l)
for x in range(8_996_453, 10 ** 7):
    d = dels(x)
    if len(d) == 2:
        if d[0] * d[1] == x:
            print(x, max(d))