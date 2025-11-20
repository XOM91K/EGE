def dels(d):
    l=[]
    for x in range(1, int(d**0.5)+1):
        if d%x==0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))
for x in range(1000, 10000):
    if sum(dels(x))%100==23:
        print(x, sum(dels(x)))