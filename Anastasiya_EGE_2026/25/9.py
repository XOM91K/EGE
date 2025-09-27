def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return sum(l)
for x in range(500_001, 10 ** 10):
    R = dels(x)
    if str(R)[-1] == '6':
        print(x, R)