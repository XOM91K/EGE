def dels(d):
    l = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            if str(x)[-1] == '7' and x != 7:
                l.append(x)
            if str(d // x)[-1] == '7' and d // x != 7:
                l.append(d // x)
    return sorted(set(l))
for x in range(700_001, 10 ** 7):
    dls = dels(x)
    if len(dls) > 0:
        print(x, min(dls))