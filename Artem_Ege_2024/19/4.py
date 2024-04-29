def g(s1,s2,p):
    if s1 + s2 >=125 and p == 3:
        return 1
    elif s1 + s2 <125 and p ==3:
        return 0
    elif s1 + s2 >=125 and p<3:
        return 0
    if p % 2 == 0:
        return g(s1+1,s2,p+1) or g(s1*4,s2,p+1) or g(s1,s2+1,p+1) or g(s1,s2 * 4,p+1)
    else:
        return g(s1+1,s2,p+1) and g(s1*4,s2,p+1) and g(s1,s2+1,p+1) and g(s1,s2 * 4,p+1)
for x in range(1,126):
    if g(7,x,0) == 1:
        print(x)