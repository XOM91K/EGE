def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    dl = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if is_prime(x):
                dl.append(x)
            if is_prime(d // x):
                dl.append(d // x)
    return sorted(dl)
ct = 0
for x in range(1_000_001, 10 ** 8):
    g = dels(x)
    if len(g) == 3:
        print(x, g[-1])
        ct += 1
    if ct == 5:
        break