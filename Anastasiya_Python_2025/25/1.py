def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    return sorted(set(dls))
for x in range(224_466, 664423):
    if x % 5 == 0 and x % 7 == 0 and x % 13 == 0:
        if x % 25 != 0 and x % 49 != 0 and x % 169 != 0:
            dls = dels(x)
            if dls[-1] < 100_000 and str(dls[-1])[-2:] == '19':
                print(x, max(dls))