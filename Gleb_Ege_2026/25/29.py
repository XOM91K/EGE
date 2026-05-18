def ip(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return n > 1
def f(n):
    l = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            if ip(x) and x % 2 != 0:
                l.append(x)
            if ip(n // x) and (n // x) % 2 != 0:
                l.append(n // x)
    return sorted(set(l))
for x in range(5000001, 10 ** 7):
    a = f(x)
    if len(a) == 2 and ip(abs(a[0] - a[1])) and a[0] * a[1] == x:
        print(x, max(a))