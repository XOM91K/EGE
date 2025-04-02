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
ct = 0
for x in range(65_001, 10 ** 10):
    if fnmatch.fnmatch(str(x), '6*97*5?'):
        lst = dels(x)
        if len(lst) >= 4:
            print(x, sum(lst))
            ct += 1
            if ct == 7:
                break