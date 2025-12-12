import fnmatch
def dels(d):
    l = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return sorted(set(l))
for x in range(23, 10 ** 6, 23):
    dls = dels(x)
    if len(dls) > 0:
        if fnmatch.fnmatch(str(dls[-1]), '*6215'):
            print(x, dls[-1])