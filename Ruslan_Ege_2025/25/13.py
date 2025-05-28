import fnmatch
def dels(n):
    r = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            r.add(i)
            r.add(n // i)
    return sorted(r)
for x in range(23, 10 ** 6, 23):
    d = dels(x)
    if len(d) > 0:
        if fnmatch.fnmatch(str(d[-1]), '*6215'):
            print(x, d[-1])