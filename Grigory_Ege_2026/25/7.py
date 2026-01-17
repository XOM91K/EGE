def dels(d):
    l = []
    for x in range(2,int(d**0.5)+1):
        if d % x == 0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))
for a in range(800001,10**7):
    g = dels(a)
    inend = [y for y in g if str(y)[-1] =='9' and y != 9]
    if len(inend)>=1:
        print(a, min(inend))