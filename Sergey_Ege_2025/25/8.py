import fnmatch
def dels(d):
    dls = []
    for x in range(1, d + 1):
        if d % x == 0:
            dls.append(x)
    return dls
for x in range(2627, 10 ** 9, 2627):
    if fnmatch.fnmatch(str(x), '7*53?3*1'):
        if len(dels(sum(map(int, str(x))))) == 2:
            print(x, x // 2627)