def dels(d):
    dl = []
    for i in range(1, int(d ** 0.5) + 1):
        if d % i == 0:
            if i % 2 == 0:
                dl.append(i)
            if (d // i) % 2 == 0:
                dl.append(d // i)
    return sorted(set(dl))
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