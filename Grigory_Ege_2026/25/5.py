def dels(d):
    l = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return sorted(set(l))
for x in range(700_001, 10 ** 6):
    M = dels(x)
    if len(M) > 1:
        M = M[0] + M[-1]
        if str(M)[-1] == '4':
            print(x, M)