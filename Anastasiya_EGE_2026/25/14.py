def dels(d):
    l = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            if str(x)[-1] == '9' and x != 9:
                l.append(x)
            if str(d // x)[-1] == '9' and (d // x) != 9:
                l.append(d // x)
    return sorted(set(l))
for x in range(800_001, 10 ** 7):
    l = dels(x)
    if len(l) > 0:
        print(x, min(l))