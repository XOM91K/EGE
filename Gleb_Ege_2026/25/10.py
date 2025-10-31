def M(d):
    l = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
            break
    return sum(l)
ct = 0
for x in range(700001, 10 ** 6):
    M2 = M(x)
    if str(M2)[-1] == '4':
        print(x, M2)
        ct += 1
        if ct == 5:
            break