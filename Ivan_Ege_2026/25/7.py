#№ 2592 (Уровень: Гроб)
def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if x % 2 != 0:
                l.append(x)
            if (d // x) % 2 != 0:
                l.append(d // x)
    return sorted(set(l))
d = []
for m in range(1, 30):
    for p in range(1, 10000):
        if 55_000_000 <= 2 ** m * p ** 4 <= 60_000_000:
            d.append(2 ** m * p ** 4)
d = sorted(set(d))
for x in d:
    l = dels(x)
    if len(l) == 5:
        print(x, l[-1])
# 2^m * p^4