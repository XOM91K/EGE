import fnmatch
def dels(d):
    l = []
    for x in range(1, int(d**0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))

for x in range(31623, 40000):
    x **= 2
    if fnmatch.fnmatch(str(x), '1*2*7*04'):
        l = dels(x)
        if len(l) == 45:
            print(x, l[-2])