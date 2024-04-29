def dels(n):
    l = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            l.append(x)
            l.append(n // x)
    return sorted(l)
for x in range(150750, 150765):
    d = dels(x)
    if len(d) == 4:
        print(d[-2], d[-1])