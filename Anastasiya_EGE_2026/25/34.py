import fnmatch
def dels(d):
    s=[]
    for x in range(1, int(d**0.5)+1):
        if d%x==0:
            s.append(x)
            s.append(d//x)
    return sorted(set(s))

for y in range(31623, 100000):
    y = y ** 2
    r=dels(y)
    if len(r)==45:
        if fnmatch.fnmatch(str(y),'1*2*7*04'):
            print(y,r[-2])