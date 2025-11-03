import fnmatch
def dels(d):
    l = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return sorted(set(l))
for x in range(23, 10 ** 6, 23):
    l = dels(x)
    if len(l) > 0 and fnmatch.fnmatch(str(l[-1]), '*6215'):
        print(x, l[-1])