def dels(n):
    dls = []
    for x in range(1, n // 2 + 1):
        if n % x == 0:
            dls.append(x)
    dls.append(n)
    return dls
d = 1_000_000_000
print(dels(d))