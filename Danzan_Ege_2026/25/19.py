def is_prime(d):
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    l = []
    for x in range(1, int(d**0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))
dd = []
for x in range(3163, 7746):
    x = x ** 2
    d = dels(x)
    if len(d) > 0 and is_prime(len(d)):
        dd.append([x, len(d)])
# print(sorted(dd, key=lambda d: -d[1]))
for x in sorted(dd, key=lambda d: -d[1]):
    print(*x)