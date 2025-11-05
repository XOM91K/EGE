def M(d):
    l = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    l = sorted(set(l))
    if len(l) > 0:
        M2 = l[0] + l[-1]
        return M2
    else:
        return 0
ct = 0
for x in range(700_001, 10 ** 7):
    M3 = M(x)
    if str(M3)[-1] == '4':
        print(x, M3)
        ct += 1
        if ct == 5:
            break