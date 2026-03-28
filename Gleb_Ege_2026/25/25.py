l = []
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return True
def f(n):
    l = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            l.append(x)
            l.append(n // x)
    return sorted(set(l))
d = []
for x in range(3162, 7746):
    x = x ** 2
    a = len(f(x))
    if is_prime(a) and a > 3:
        d.append([x, a])
d = sorted(d, key=lambda r: -r[1])
for x in d:
    print(*x)