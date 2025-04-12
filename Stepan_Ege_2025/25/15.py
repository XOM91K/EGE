import fnmatch
def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
                dls.append(x)
                dls.append(n // x)
    dls = sorted(set(dls))
    if len(dls) > 0:
        return max(dls)
    else:
        return 0
for x in range(23, 10 ** 6, 23):
    d = dels(x)
    if fnmatch.fnmatch(str(d), '*6215'):
        print(x, d)