def dels(d):
    l = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return sorted(set(l))
for x in range(110_250_000, 110_300_001):
    l = dels(x)
    if len(l) > 1:
        M = l[-1] + l[-2]
        if str(M)[-4:] == '1002' and M % 10000 == 1002:
            print(x)