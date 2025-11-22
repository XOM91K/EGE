def dels(d):
    l=[]
    for x in range(2, int(d**0.5)+1):
        if d%x==0:
            if x != 7 and str(x)[-1] == '7':
                l.append(x)
            if (d // x) != 7 and str(d // x)[-1] == '7':
                l.append(d//x)
    return sorted(set(l))
ct = 0
for y in range(1_125_001,10**10):
    m=dels(y)
    if len(m)>0:
            print(y, min(m))
            ct += 1
            if ct == 5:
                break