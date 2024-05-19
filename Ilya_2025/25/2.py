import fnmatch

def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    return sorted(set(dls))
for x in range(23, 10 ** 6, 23):
    mx = dels(x)[-2]
    if fnmatch.fnmatch(str(mx), '*6215'):
        print(x, mx)