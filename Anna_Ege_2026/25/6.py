import fnmatch
def dels(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    if len(dls) == 0:
        return 0
    else:
        return max(dls)
for x in range(23, 10**6, 23):
    mxdl = dels(x)
    if fnmatch.fnmatch(str(mxdl),'*6215'):
        print(x, mxdl)