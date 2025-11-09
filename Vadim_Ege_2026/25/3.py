import fnmatch
def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if x % 2 == 0:
                l.append(x)
            if (d // x) % 2 == 0:
                l.append(d // x)
    return sorted(set(l))
for x in range(65001, 10 ** 7):
    l = dels(x)
    if len(l) >= 4 and fnmatch.fnmatch(str(x), '6*97*5?'):
        print(x, sum(l))
