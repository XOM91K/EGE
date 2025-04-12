def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    return sorted(set(dls))
for x in range(10332, 12356):
    x **= 2
    dl = dels(x)
    if len(dl) == 3:
        print(x, max(dl))