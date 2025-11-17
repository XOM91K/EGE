def f(s1,s2,p):#19
    if s1+s2 >= 212 and p == 1:
        return 1
    if s1+s2 < 212 and p ==1:
        return 0
    if s1+s2 >= 212 and p <1:
        return 0
    if p%2==0:
        return f(s1+s2,s2,p+1) or f(s1,s1+s2,p+1)
    else:
        return f(s1+s2,s2,p+1) or f(s1,s1+s2,p+1)
for s in range(0,111):
    if f(100,s,0) == False:
        print(s)