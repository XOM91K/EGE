def f(d):
    a = set()
    for i in range(2, int(d ** 0.5) + 1):
        if d % i == 0:
            if i % 2 != 0:
                a.add(i)
            if (d // i) % 2 != 0:
                a.add(d // i)
    return sorted(a)
for x in range(18782, 18823):
    g = f(x)
    if len(g) == 3:
        print(*g)