import fnmatch
def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return sorted(set(l))
for x in range(23, 10 ** 6, 23):
    dl = dels(x)
    if fnmatch.fnmatch(str(dl[-2]), '*6215'):
        print(x, dl[-2])