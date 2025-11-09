# def F(s,p):#19
#     if s >= 84 and p==2:
#         return 1
#     if s < 84 and p == 2:
#         return 0
#     if s >= 84 and p < 2:
#         return 0
#     if p%2==0:
#         return F(s+1,p+1) and F(s*1.5 if s%2==0 else s*2,p+1)
#     else:
#         return F(s+1,p+1) or F(s*1.5 if s%2==0 else s*2,p+1)
# for s in range(0,84):
#     if F(s,0):
#         print(s)


# def F(s,p):#19
#     if s >= 84 and p==3:
#         return 1
#     if s < 84 and p == 3:
#         return 0
#     if s >= 84 and p < 3:
#         return 0
#     if p%2!=0:
#         return F(s+1,p+1) and F(s*1.5 if s%2==0 else s*2,p+1)
#     else:
#         return F(s+1,p+1) or F(s*1.5 if s%2==0 else s*2,p+1)
# for s in range(0,84):
#     if F(s,0):
#         print(s)

def F(s,p):#19
    if s >= 84 and (p==2 or p == 4):
        return 1
    if s < 84 and p == 4:
        return 0
    if s >= 84 and p < 4:
        return 0
    if p%2==0:
        return F(s+1,p+1) and F(s*1.5 if s%2==0 else s*2,p+1)
    else:
        return F(s+1,p+1) or F(s*1.5 if s%2==0 else s*2,p+1)
for s in range(0,84):
    if F(s,0):
        print(s)
# def F(s,p):#20
#     if s >= 84 and p==3:
#         return 1
#     if s < 84 and p == 3:
#         return 0
#     if s >= 84 and p < 3:
#         return 0
#     if p%2==0:
#         return F(s+1,p+1) or F(s*2 if s%2==0 else s*1.5,p+1)
#     else:
#         return F(s+1,p+1) and F(s*2 if s%2==0 else s*1.5,p+1)
# for s in range(0,84):
#     if F(s,0):
#         print(s)
#
# def F(s,p):#21
#     if s >= 84 and (p==4 or p == 2):
#         return 1
#     if s < 84 and p == 4:
#         return 0
#     if s >= 84 and p % 2 != 0:
#         return 0
#     if p%2!=0:
#         return F(s+1,p+1) or F(s*2 if s%2==0 else s*1.5,p+1)
#     else:
#         return F(s+1,p+1) and F(s*2 if s%2==0 else s*1.5,p+1)
# for s in range(0,84):
#     if F(s,0):
#         print(s)