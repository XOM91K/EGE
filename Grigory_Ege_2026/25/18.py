import fnmatch
def dels(d):
    l = []
    for x in range(1,int(d**0.5)+1):
        if d % x == 0 :
            l.append(x)
            l.append(d//x)
    return sorted(set(l))
for x in range(31_623,50_000):
    x = x ** 2
    if fnmatch.fnmatch(str(x),'1*2*7*04'):
        n = dels(x)
        if len(n) == 45:
            print(x, sorted(n)[-2])