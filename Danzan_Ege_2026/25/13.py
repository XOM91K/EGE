def dels(d):
    l = []
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))
for x in range(700000, 1, -1):
    l = dels(x)
    if len(l) > 0:
        M = sum(l)//len(l)
        if str(M)[-3:] == '313':
            print(x, M)