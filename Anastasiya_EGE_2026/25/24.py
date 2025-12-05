import fnmatch
def dels(d):
    l=[]
    for x in range(1, int(d**0.5)+1):
        if d%x==0:
            if fnmatch.fnmatch(str(x), '2*3?'):
                l.append(x)
            if fnmatch.fnmatch(str(d // x), '2*3?'):
                l.append(d//x)
    return sorted(set(l))
# [1, 5, 10, 12, 19]
for y in range(500001, 10**10):
        if len(dels(y)) >= 1:
            print(y, min(dels(y)))