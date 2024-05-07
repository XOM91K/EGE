import fnmatch
def delss(d):
    dels = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            dels.append(x)
            dels.append(d // x)
    return sorted(set(dels))
for x in range(109, 10 ** 9, 100):
    if fnmatch.fnmatch(str(x), '15*3*09'):
        d = delss(x)
        if len(d) == 9:
            print(x, d[-2])