import fnmatch
def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    if len(dls) > 0:
        return max(sorted(set(dls)))
    else:
        return 0
for x in range(23, 10 ** 6, 23):
    mxdl = dels(x)
    if fnmatch.fnmatch(str(mxdl), '*6215'):
        print(x, mxdl)