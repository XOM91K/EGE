def dels(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    if len(dls) > 0:
        return max(dls) - min(dls)
    else:
        return 0
for x in range(1_533_878, 0, -1):
    F = dels(x)
    if F > 5000 and F % 1235 == 0:
        print(x, F)