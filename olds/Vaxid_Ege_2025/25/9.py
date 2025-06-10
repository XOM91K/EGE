def dels(n):
    dls = []
    for x in range(2, n):
        if n % x == 0 and x % 2 != 0:
            dls.append(x)
    return dls
for x in range(18782, 18823):
    dls = dels(x)
    if len(dls) == 3:
        print(*dls)