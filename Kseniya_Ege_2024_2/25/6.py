import fnmatch
def delss(d):
    dels = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if x % 2 == 0:
                dels.append(x)
            if (d // x) % 2 == 0:
                dels.append(d // x)
    return sorted(set(dels))
ct = 0
for x in range(65001, 1000000):
    if fnmatch.fnmatch(str(x), '6*97*5?'):
        if len(delss(x)) >= 4:
            print(x, sum(delss(x)))
            ct += 1
    if ct == 7:
        break