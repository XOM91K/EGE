def is_prime(d):
    for x in range(2, (int(d ** 0.5)) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if str(x).count('3') == 2 and is_prime(x):
                dls.append(x)
            if str(d // x).count('3') == 2 and is_prime(d // x):
                dls.append(d // x)
    return sorted(set(dls))
for x in range(8_996_453, 10 ** 7):
    dls = dels(x)
    if len(dls) == 2 and dls[0] * dls[1] == x:
        print(x, max(dls))