def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if x % 2 == 0:
                dls.append(x)
            if (d // x) % 2 == 0:
                dls.append(d // x)
    return sorted(set(dls))
ct = 0
import fnmatch
for x in range(65001, 10 ** 8):
    if fnmatch.fnmatch(str(x), '6*97*5?'):
        g = dels(x)
        if len(g) >= 4:
            print(x, sum(g))
            ct += 1
        if ct == 7:
            break