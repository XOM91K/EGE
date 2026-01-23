def dels(d):
    l = []
    for x in range(1, int(d**0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))
for x in range(10_000, 31_623):
    x = x ** 2
    print(x)
    if x % 2 == 0:
        d = dels(x)
        if len(d) == 39:
            mx = max([x for x in d if x%2 != 0])
            print(x, mx)
