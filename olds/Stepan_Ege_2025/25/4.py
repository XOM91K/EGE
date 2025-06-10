def dels(n):
    dls = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    return sorted(set(dls))
print(dels(144))
