def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x  == 0:
            l.append(x)
            l.append(d // x)
    return sorted(set(l))
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
d = []
for x in range(3163, 7746):
    x = x ** 2
    dls = dels(x)
    if is_prime(len(dls)):
        d.append([x, len(dls)])
print(sorted(d, key=lambda d: -d[1]))
for x in sorted(d, key=lambda d: -d[1]):
    print(*x)