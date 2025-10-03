import fnmatch #zadacha iz dz
def dels(d):
    l=[]
    for x in range(1, int(d**0.5)+1):
        if d%x==0:
            if x % 2 == 0:
                l.append(x)
            if (d // x) % 2 == 0:
                l.append(d//x)
    return l

for y in range(65000, 10**10):
    if fnmatch.fnmatch(str(y), '6*97*5?'):
        if len(dels(y)) >= 4:
            print(y, sum(dels(y)))