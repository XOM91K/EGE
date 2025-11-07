import fnmatch
def m(n):
    l = []
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            if d % 2 == 0:
                l.append(d)
            if (n // d) % 2 == 0:
                l.append(n // d)
    return l
ct = 0
for x in range(65001, 11500_000):
    l = m(x)
    if fnmatch.fnmatch(str(x), '6*97*5?') and len(l) >= 4:
        print(x, sum(m(x)))