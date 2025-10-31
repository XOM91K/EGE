def M(d):
    l = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    l = sorted(set(l))
    return l[-1] + l[-2] if len(l) >= 2 else 0
for x in range(112_500_000, 112_550_001):
    r = M(x)
    if str(r)[-4:] == '1214':
        print(x)