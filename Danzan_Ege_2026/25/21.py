def dels(d):
    l = []
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))
for x in range(1, 32623):
    x = x ** 2
    if x % 106 == 0:
        l = dels(x)
        if len(l) == 7:
            print(x, max(l))