def F(s,p):#20
    if s <= 19 and p==3:
        return 1
    if s > 19 and p == 3:
        return 0
    if s <= 19 and p < 3:
        return 0
    if p % 2 != 0:
        return F(s-1,p+1) and F(s // 3 if s % 3 == 0 else s - 2 ,p+1) and F(s // 5 if s % 5 == 0 else s - 3,p+1)
    else:
        return F(s-1,p+1) or F(s // 3 if s % 3 == 0 else s - 2 ,p+1) or F(s // 5 if s % 5 == 0 else s - 3,p+1)
for x in range(20,500):
    if F(x,0) == 1:
        print(x)