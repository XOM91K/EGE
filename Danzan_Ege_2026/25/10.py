def dels(d):
    l = []
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))
for x in range(900_001, 950_000):
    MN = dels(x)
    if len(MN) > 1:
        MN = MN[0] + MN[-1]
        if str(MN)[-2:] == '46':
            print(x, MN)