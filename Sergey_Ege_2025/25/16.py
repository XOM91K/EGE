def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            if str(x)[-1] == '7' and x != 7:
                dls.append(x)
            if str(n // x)[-1] == '7':
                dls.append(n // x)
    if len(dls) == 0:
        return 0
    else:
        return min(dls)
for x in range(1_125_000, 100_000_000):
    f = dels(x)
    if f != 0:
        print(x, f)