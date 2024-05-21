def dels(n):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    return sorted(set(dls))

d = 625
print(dels(d))
