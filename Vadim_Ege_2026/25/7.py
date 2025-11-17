import fnmatch


def dels(x):
    k = []
    for y in range(1, int(x ** 0.5) + 1):
        if x % y == 0:
            k.append(x // y)
            k.append(y)
    return sorted(set(k))


for x in range(999, 9999):
    b = dels(x)
    if len(b) >= 2:
        m = sum(b)
        if m % 100 == 23:
            print(x, m)
