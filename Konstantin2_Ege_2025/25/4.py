import fnmatch
def dels(n):
    dls = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    return sorted(set(dls))
for x in range(23, 10 ** 6, 23):
    dl = dels(x)
    if fnmatch.fnmatch(str(dl[-2]), '*6215'):
        print(x, dl[-2])