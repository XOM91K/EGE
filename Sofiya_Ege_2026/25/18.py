def dels(d):
    l = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return sorted(set(l))

import fnmatch
for x in range(23, 10**6, 23):
    if len(dels(x)) > 0:
        if fnmatch.fnmatch(str(max(dels(x))), '*6215'):
            print(x,max(dels(x)))