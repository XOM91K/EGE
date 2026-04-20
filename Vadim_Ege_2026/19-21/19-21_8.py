def F(s,p):#21
    if s >= 77 and (p==4 or p == 2):
        return 1
    if s < 77 and p == 4:
        return 0
    if s >= 77 and p < 4:
        return 0
    if p%2!=0:
        return F(s+1,p+1) or F(s + 4,p+1) or F(s * 2,p+1)
    else:
        return F(s+1,p+1) and F(s + 4,p+1) and F(s * 2,p+1)
for s in range(1,78):
    if F(s,0):
        print(s)