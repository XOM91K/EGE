def f(n):
    l = []
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            l.append(d)
            l.append(n // d)
    return sorted(set(l))
for x in range(1, 31623):
    x = x ** 2
    if x % 106 == 0:
        F = f(x)
        if len(F) == 7:
            print(x, F[-1])