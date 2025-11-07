def m(n):
    l = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            l.append(x)
            l.append(n // x)
    l = sorted(set(l))
    return l[-1] + l[-2] if len(l) >= 2 else 0
for N in range(110_250_000, 110_300_000):
    if str(m(N))[-4:] == '1002':
        print(N, m(N))