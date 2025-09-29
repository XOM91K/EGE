import fnmatch

def dels(d):
    r = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            r.append(x)
            r.append(d // x)
    return list(set(r))
for x in range(53, 10 ** 7, 53):
    r = dels(x)
    if fnmatch.fnmatch(str(x), '*2?2*'):
        if len(r) > 30 and str(x) == str(x)[::-1]:
            print(x, sum(r))