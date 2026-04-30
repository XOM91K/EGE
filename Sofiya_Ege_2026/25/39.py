def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1


def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if is_prime(x):
                l.append(x)
            if is_prime(d // x):
                l.append(d // x)
    return sorted(l)


for x in range(20262027, 10 ** 9):
    l = dels(x)
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 2026:
                print(x, max(l))
