def dels(d):
    l = []
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))

for x in range(1125_000, 10**10):
    l = dels(x)
    mn7 = []
    for y in l:
        if str(y)[-1] == '7' and y != x and y != 7:
            mn7.append(y)
    if len(mn7) > 0:
        print(x, min(mn7))