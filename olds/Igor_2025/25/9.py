import fnmatch
def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    return len(set(dls))
for x in range(10_000, 14_142):
    x **= 2
    if fnmatch.fnmatch(str(x), '?*42*81'):
        if dels(x) == 3:
            print(x)