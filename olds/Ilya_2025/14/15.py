def dvp(n):
    s=[]
    while n>0:
        s.append(n % 25)
        n//=25
    return s[::-1]
for x in range(1, 2500+1):
    st = 25**150+25**100-x
    ct0 = dvp(st).count(0)
    if ct0 >= 52:
        print(x, ct0)