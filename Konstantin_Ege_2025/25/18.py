def M(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    dls = sorted(set(dls))
    if len(dls) > 0:
        MM = dls[0] + dls[-1]
        return MM
    else:
        return 0
for x in range(800000, 10 ** 10):
    M2 = M(x)
    if M2 % 10 == 4:
        print(x, M2)