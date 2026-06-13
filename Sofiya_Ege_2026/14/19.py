def f11(n):
    s=[]
    while n>0:
        s.append(n%11)
        n//=11
    return s
for x in range(3001):
    a=9*11**210+8*11**150-x
    b=f11(a)
    if b.count(0)==60:
        print(x)