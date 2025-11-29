def m(n):
    l = []
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            l.append(d)
            l.append(n // d)
    return sorted(set(l))
for x in range(1000, 10000):
    a = m(x)
    if str(sum(a))[-2:] == '23':
        print(x, sum(a))