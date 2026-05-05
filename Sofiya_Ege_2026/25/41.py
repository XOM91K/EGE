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
                if x % 2 != 0:
                    l.append(x)
            if is_prime(d // x):
                if (d // x) % 2 != 0:
                    l.append(d // x)
    return sorted(set(l))


for x in range(5_000_001, 10 ** 7, 2):
    l = dels(x)
    if len(l) == 2 and l[0] * l[1] == x:
        if is_prime(abs(l[0] - l[1])):
            print(x, max(l))
