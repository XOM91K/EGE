# # def g(s,p):
# #     if s <= 25 and p == 2:
# #         return 1
# #     elif s <= 25 and p < 2:
# #         return 0
# #     elif s > 25 and p == 2:
# #         return 0
# #     if p % 2 == 0:
# #         return g(s-4,p+1) and g(s-6,p+1) and g(s//3,p+1)
# #     else:
# #         return g(s - 4 , p + 1) or g(s - 6 , p + 1) or g(s // 3 , p + 1)
# # for S in range(26,10000):
# #     if g(S,0):
# #         print(S)
#
# def g(s,p):
#     if s <= 25 and p == 3:
#         return 1
#     elif s <= 25 and p < 3:
#         return 0
#     elif s > 25 and p == 3:
#         return 0
#     if p % 2 != 0:
#         return g(s-4,p+1) and g(s-6,p+1) and g(s//3,p+1)
#     else:
#         return g(s - 4 , p + 1) or g(s - 6 , p + 1) or g(s // 3 , p + 1)
# for S in range(26,10000):
#     if g(S,0):
#         print(S)

def g(s, p):
    if s <= 25 and (p == 2 or p == 4):
        return 1
    elif s > 25 and p == 2:
        return 0
    elif s <= 25 and p < 4:
        return 0
    if p % 2 == 0:
        return g(s - 4, p + 1) and g(s - 6, p + 1) and g(s // 3, p + 1)
    else:
        return g(s - 4, p + 1) or g(s - 6, p + 1) or g(s // 3, p + 1)


for S in range(26, 10000):
    if g(S, 0):
        print(S)
# 78
# 79
# 80
# 81
# 88
# 89
# 90
# 91
# 246
# 247
# 248
# 249