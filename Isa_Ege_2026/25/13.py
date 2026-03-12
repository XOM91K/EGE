import fnmatch
def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if x % 2 == 0:
                dls.append(x)
            if (d // x) % 2 == 0:
                dls.append(d // x)
    return sorted(set(dls))
for x in range(65001, 10 ** 8):
    dls = dels(x)
    # шаблоном pattern
    if len(dls) >= 4 and fnmatch.fnmatch(str(x), '6*97*5?'):
        print(x, sum(dls))