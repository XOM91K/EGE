def dels(d):
    dls = []
    for i in range(2, int(d ** 0.5) + 1):
        if d % i == 0:
            dls.append(i)
            dls.append(d // i)
    dl = sorted(set(dls))
    if len(dl) >= 2:
        return dl[-1] + dl[-2]
    else:
        return 0

for x in range(112500000, 112550001):
    c = dels(x)
    if str(c)[-4:] == '1214':
        print(x)
