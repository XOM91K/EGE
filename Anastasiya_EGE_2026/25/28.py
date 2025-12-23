def dels(d):
    l=[]
    for x in range(2, int(d**0.5)+1):
        if d%x==0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))
for y in range(1533878,1,-1):
    f=dels(y)
    if len(f)>1:
        f=f[-1]-f[0]
        if f>5000 and f%1235==0:
            print(y, f)

# 1533874 766935
# 1531404 765700
# 1528934 764465
# 1526469 508820
# 1526464 763230
1526464 763230
1526469 508820
1528934 764465
1531404 765700
1533874 766935