def dels(d):
    l = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return sorted(set(l))
for x in range(112_500_000, 112_550_001):
    MN = dels(x)
    if len(MN) > 1:
        MN = MN[-1] + MN[-2]
        if str(MN)[-4:] == '1214':
            print(x)