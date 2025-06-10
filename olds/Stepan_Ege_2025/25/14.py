import fnmatch
def dels(n):
    dls = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            if x % 2 == 0:
                dls.append(x)
            if (n // x) % 2 == 0:
                dls.append(n // x)
    return sorted(set(dls))
for x in range(65001, 10 ** 10):
    if fnmatch.fnmatch(str(x), '6*97*5?'):
        d = dels(x)
        if len(d) >= 4:
            print(x, sum(d))