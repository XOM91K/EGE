def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if is_prime(x) and (str(x).count('1') == 2):
                dls.append(x)
            if is_prime(d // x) and (str(d // x).count('1') == 2):
                dls.append(d // x)
    return sorted((dls))
for x in range(8_568_642, 10 ** 7):
    dls = dels(x)
    if len(dls) >= 2:
        if dls[0] * dls[1] == x:
            print(x, max(dls))