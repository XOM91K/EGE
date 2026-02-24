# def g(s, p):
#     if s <= 31 and p == 2:
#         return 1
#     elif s > 31 and p == 2:
#         return 0
#     elif s <= 31 and p < 2:
#         return 0
#     if p % 2 == 0:
#         if s % 4 == 0:
#             return g(s - 2, p + 1) and g(s - 3, p + 1) and g(s // 4, p + 1)
#         else:
#             return g(s - 2, p + 1) and g(s - 3, p + 1)
#     else:
#         if s % 4 == 0:
#             return g(s - 2, p + 1) or g(s - 3, p + 1) or g(s // 4, p + 1)
#         else:
#             return g(s - 2, p + 1) or g(s - 3, p + 1)
#
#
# for S in range(32, 10000):
#     if g(S, 0):
#         print(S)
def g(s, p):
    if s <= 31 and (p == 2 or p == 4):
        return 1
    elif s > 31 and p == 4:
        return 0
    elif s <= 31 and p < 4:
        return 0
    if p % 2 == 0:
        if s % 4 == 0:
            return g(s - 2, p + 1) and g(s - 3, p + 1) and g(s // 4, p + 1)
        else:
            return g(s - 2, p + 1) and g(s - 3, p + 1)
    else:
        if s % 4 == 0:
            return g(s - 2, p + 1) or g(s - 3, p + 1) or g(s // 4, p + 1)
        else:
            return g(s - 2, p + 1) or g(s - 3, p + 1)


for S in range(32, 10000):
    if g(S, 0):
        print(S)
