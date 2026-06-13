A = []
def F(s,p):
    if  s >= 150 and (p == 2 or p == 4):
        return 1
    if s < 150 and p == 4:
        return 0
    if s >= 150 and p < 4:
        return 0
    if p % 2 == 0 :
        return F(s+4,p+1) and F(s+8,p+1) and F(s*3 ,p+1)
    else:
        return F(s+4,p+1) or F(s+8,p+1) or F(s*3 ,p+1)
for S in range(1,150):
    if F(S,0):
        print(S)