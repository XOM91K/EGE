def dels(n):
    l = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            l.append(x)
            l.append(n // x)
    return sorted(set(l))
for x in range(193136, 193234):
    if len(dels(x)) == 6:
        print(dels(x)[-2], x)