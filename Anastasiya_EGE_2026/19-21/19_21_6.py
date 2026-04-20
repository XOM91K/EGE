import math
# print(math.ceil(4.2))
# def g(s1, s2, p):
#     if s1 + s2 <= 60 and p == 2:
#         return 1
#     elif s1 + s2 > 60 and p == 2:
#         return 0
#     elif s1 + s2 <= 60 and p < 2:
#         return 0
#     if p % 2 == 0:
#         return g(s1 - 5, s2, p + 1) or g(s1, s2 - 3, p + 1) or g(s1 // 2, s2, p + 1) or g(s1, math.ceil(s2 / 2), p + 1)
#     else:
#         return g(s1 - 5, s2, p + 1) or g(s1, s2 - 3, p + 1) or g(s1 // 2, s2, p + 1) or g(s1, math.ceil(s2 / 2), p + 1)
# for S in range(5, 151):
#     if g(130, S, 0):
#         print(S)
# 28
# def g(s1, s2, p):
#     if s1 + s2 <= 60 and p == 3:
#         return 1
#     elif s1 + s2 > 60 and p == 3:
#         return 0
#     elif s1 + s2 <= 60 and p < 3:
#         return 0
#     if p % 2 == 0:
#         return g(s1 - 5, s2, p + 1) or g(s1, s2 - 3, p + 1) or g(s1 // 2, s2, p + 1) or g(s1, math.ceil(s2 / 2), p + 1)
#     else:
#         return g(s1 - 5, s2, p + 1) and g(s1, s2 - 3, p + 1) and g(s1 // 2, s2, p + 1) and g(s1, math.ceil(s2 / 2), p + 1)
# for S in range(5, 151):
#     if g(130, S, 0):
#         print(S)
# 28
# 29 30
# 27 * 26
def g(s1, s2, p):
    if s1 + s2 <= 60 and (p == 1 or p == 3 or p == 5):
        return 1
    elif s1 + s2 > 60 and p == 5:
        return 0
    elif s1 + s2 <= 60 and p < 5:
        return 0
    if p % 2 == 0:
        return g(s1 - 5, s2, p + 1) or g(s1, s2 - 3, p + 1) or g(s1 // 2, s2, p + 1) or g(s1, math.ceil(s2 / 2), p + 1)
    else:
        return g(s1 - 5, s2, p + 1) and g(s1, s2 - 3, p + 1) and g(s1 // 2, s2, p + 1) and g(s1, math.ceil(s2 / 2), p + 1)
for S in range(5, 151):
    if g(130, S, 0):
        print(S)
print(34*35*36*61*62)