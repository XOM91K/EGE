def dels(x):
    k = []
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            k.append(d)
            k.append(x // d)
        if len(set(k)) == 8:
            return k
    return k


for x in range(31623):
    x = x ** 2
    if x % 106 == 0:
        k = dels(x)
        if len(set(k)) == 7:
            print(x, max(k))
