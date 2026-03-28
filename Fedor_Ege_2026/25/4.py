def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return sorted(set(l))
for x in range(201_455, 201_471):
    dls = dels(x)
    if len(dls) == 4:
        print(*dls)