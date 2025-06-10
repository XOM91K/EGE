import fnmatch
def max_del(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    dls = sorted(set(dls))
    if len(dls) > 0:
        return dls[-1]
    else:
        return -1
for x in range(0, 10 ** 6, 23):
    mx_del = max_del(x)
    if fnmatch.fnmatch(str(mx_del), '*6215'):
        print(x, mx_del)