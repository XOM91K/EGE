# def F(s,p):
#     if s >= 150 and p == 2:
#         return 1
#     if s < 150 and p == 2:
#         return 0
#     if s >= 150 and p < 2:
#         return 0
#     if p%2==0:
#         return F(s+8,p+1) and F(s+4,p+1) and F(s*3,p+1)
#     else:
#         return F(s+8,p+1) or F(s+4,p+1) or F(s*3,p+1)
# for s in range(0,150):
#     if F(s,0):
#         print(s)
def F(s,p):
    if s >= 150 and p == 3:
        return 1
    if s < 150 and p == 3:
        return 0
    if s >= 150 and p < 3:
        return 0
    if p%2!=0:
        return F(s+8,p+1) and F(s+4,p+1) and F(s*3,p+1)
    else:
        return F(s+8,p+1) or F(s+4,p+1) or F(s*3,p+1)
for s in range(0,150):
    if F(s,0):
        print(s)