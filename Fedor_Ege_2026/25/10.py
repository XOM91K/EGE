def dels(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            if x != 11 and str(x)[-2:] == '11':
                dls.append(x)
            if (d // x) != 11 and str(d // x)[-2:] == '11':
                dls.append(d // x)
    return sorted(set(dls))
for x in range(1_350_051, 10 ** 10):
    F = dels(x)
    if len(F) > 0:
        print(x, F[0])