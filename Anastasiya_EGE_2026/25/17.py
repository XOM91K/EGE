def dels(d):
    l=[]
    for x in range(1, int(d**0.5)+1):
        if d%x==0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))
for y in range(201455, 201471):
    z=dels(y)
    if len(z)==4:
        print(*z)