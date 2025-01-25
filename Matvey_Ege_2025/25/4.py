import fnmatch
def dels(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            if x % 2 == 0:
                dls.append(x)
            if (d // x) % 2 == 0:
                dls.append(d // x)
    return sorted(set(dls))

for x in range(65000, 10 ** 8):
    c = dels(x)
    if fnmatch.fnmatch(str(x), '6*97*5'):
       if len(c) >= 4:
           print(x, sum(c))