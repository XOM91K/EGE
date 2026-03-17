# def g(s1, s2, p):
#     if (s1 * s2) >= 415 and p == 2:
#         return 1
#     if (s1 * s2) < 415 and p == 2:
#         return 0
#     if (s1 * s2) >= 415 and p < 2:
#         return 0
#     if p % 2 == 0:
#         return g(s1 + 3, s2, p + 1) or g(s1 + 17, s2, p + 1) or g(s1, s2 + 3, p + 1) or g(s1, s2 + 17, p + 1)
#     else:
#         return g(s1 + 3, s2, p + 1) or g(s1 + 17, s2, p + 1) or g(s1, s2 + 3, p + 1) or g(s1, s2 + 17, p + 1)
# ct = 0
# for S in range(1, 52):
#     if g(8, S, 0):
#         ct += 1
# print(ct)
def g(s1,s2,p):
    if (s1*s2)>=415 and (p==2 or p==4):
        return 1
    if (s1*s2)<415 and p==4:
        return 0
    if (s1*s2)>=415 and p<4:
        return 0
    if p%2==0:
        return g(s1+3,s2,p+1)  and g(s1+17,s2,p+1) and g(s1,s2+3,p+1) and g(s1,s2+17,p+1)
    else:
        return g(s1 + 3, s2, p+1) or g(s1 + 17, s2, p+1) or g(s1, s2 + 3, p+1) or g(s1, s2 + 17, p+1)
for S in range(1,52):
    if g(8,S,0):
        print(S)
