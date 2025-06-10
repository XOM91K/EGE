def dels(d):
    dls = []
    for i in range(1, int(d ** 0.5) + 1):
        if d % i == 0:
            dls.append(i)
            dls.append(d // i)
    return sorted(set(dls))
for i in range(1_125_000, 10 ** 10):
    o = 0
    can = False
    s = dels(i)
    for j in s:
        if str(j)[-1] == '7' and j != i and j != 7:
            o = j
            can = True
            break
    if can:
        print(i, o)