def dels(d):
    dls = []
    for x in range(1,int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d//x)
    return sorted(set(dls))
l = []
for x in range(10_000, 31_622):
    x = x ** 2
    if x % 2 == 0:
        dls = dels(x)
        if len(dls) == 39:
            c = max([y for y in dls if y % 2 != 0])
            l.append([x,c])
