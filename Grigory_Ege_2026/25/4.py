def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return sum(sorted(set(l)))
for x in range(1000, 10000):
    S = dels(x)
    if str(S)[-2:] == '23':
        print(x, S)
