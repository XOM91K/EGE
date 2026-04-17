def dels(d):
    dls=[]
    for x in range(2, int(d**0.5)+1):
        if d % x == 0:
            dls.append(x)
            dls.append(d//x)
    return sorted(set(dls))
for x in range(1, 32000):
    x = x ** 2
    if x%106==0:
        l=dels(x)
        if len(l)==7:
            print(x, max(l))