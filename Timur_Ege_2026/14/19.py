def v15(d):
    s=[]
    while d>0:
        s.append(str(d%15))
        d//=15
    return s
for x in range(1,10000000):
    c=15**450+15**100-11123471-x
    c=v15(c)
    if x%11==0 and c.count('14')==97:
        print(x)