def f11(n):
    s=[]
    while n>0:
        s.append(n%11)
        n//=11
    return s[::-1]
for x in range(3, 1000000, 3):
    a=11**250+11**5-358123-x
    b=f11(a)
    if b.count(10)==248:
        print(x)