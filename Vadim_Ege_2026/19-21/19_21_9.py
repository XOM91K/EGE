def f(s,p):#19
    if s>=81 and p == 2:
        return 1
    if s>=81 and p == 1:
        return 0
    if s<81 and p == 2:
        return 0
    if p%2==0:
        return f(s+1,p+1) or f(s*2,p+1)
    else:
        return f(s+1,p+1) or f(s*2,p+1)
for x in range(1,74):
    if f(x,0) == 1:
        print(x)