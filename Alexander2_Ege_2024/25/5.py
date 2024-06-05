def dels(n):
    dl = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dl.append(x)
            dl.append(n // x)
    return sorted(set(dl))
ct = 0
for x in range(460_000_001, 470_000_000):
    d = dels(x) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    MN = 0
    if len(d) >= 5:
        MN = d[-5]
        print(MN, x)
        ct += 1
    if ct == 5:
        break