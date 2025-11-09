# # def F(s,p):#19
# #     if s >= 56 and p == 2:
# #         return 1
# #     if s < 56 and p == 2:
# #         return 0
# #     if s >= 56 and p < 2:
# #         return 0
# #     if p%2==0:
# #         return F(s+4,p+1) or F(s+5,p+1) or (F(s*3,p+1) if s%3==0 else 0)
# #     else:
# #         return F(s+4,p+1) or F(s+5,p+1) or (F(s*3,p+1) if s%3==0 else 0)
# # for s in range(0,55):
# #     if F(s,0):
# #         print(s)
#
# def F(s,p):#20
#     if s >= 56 and p == 3:
#         return 1
#     if s < 56 and p == 3:
#         return 0
#     if s >= 56 and p < 3:
#         return 0
#     if p%2==0:
#         if s % 3 == 0:
#             return F(s+1,p+1) or F(s+2,p+1) or F(s*3,p+1)
#         else:
#             return F(s + 1, p + 1) or F(s + 2, p + 1)
#     else:
#         if s % 3 == 0:
#             return F(s + 1, p + 1) and F(s + 2, p + 1) and F(s * 3, p + 1)
#         else:
#             return F(s + 1, p + 1) and F(s + 2, p + 1)
# for s in range(0,55):
#     if F(s,0):
#         print('20:', s)#ничего не выводит

def F(s,p):#21
    if s >= 56 and (p == 4 or p ==6 or p==2):#позже убрать 2 и 4
        return 1
    if s < 56 and p == 6:
        return 0
    if s >= 56 and p < 6:
        return 0
    if p%2!=0:
        if s % 3 == 0:
            return F(s+1,p+1) or F(s+2,p+1) or F(s*3,p+1)
        else:
            return F(s + 1, p + 1) or F(s + 2, p + 1)
    else:
        if s % 3 == 0:
            return F(s + 1, p + 1) and F(s + 2, p + 1) and F(s * 3, p + 1)
        else:
            return F(s + 1, p + 1) and F(s + 2, p + 1)
for s in range(0,55):
    if F(s,0):
        print(s)