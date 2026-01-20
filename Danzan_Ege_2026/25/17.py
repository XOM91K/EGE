import fnmatch
def dels(d):
    l = []
    for x in range(1, int(d**0.5) + 1):
        if d % x == 0:
            if fnmatch.fnmatch(str(x), '2*3?'):
                l.append(x)
            if fnmatch.fnmatch(str(d // x), '2*3?'):
                l.append(d // x)
    return sorted(set(l))
for x in range(500_001, 1_000_000):
    l = dels(x)
    if len(l) > 0:
        print(x, min(l))