# def g(s, p):
#     if s <= 17 and p == 2:
#         return 1
#     elif s > 17 and p == 2:
#         return 0
#     elif s <= 17 and p < 2:
#         return 0
#     if p % 2 == 0:
#         if s % 3 == 0 and s % 5 == 0:
#             return g(s - 1, p + 1) and g(s // 3, p + 1) and g(s // 5, p + 1)
#         elif s % 3 == 0:
#             return g(s - 1, p + 1) and g(s // 3, p + 1) and g(s - 3, p + 1)
#         elif s % 5 == 0:
#             return g(s - 1, p + 1) and g(s - 2, p + 1) and g(s // 5, p + 1)
#         else:
#             return g(s - 1, p + 1) and g(s - 2, p + 1) and g(s - 3, p + 1)
#     else:
#         if s % 3 == 0 and s % 5 == 0:
#             return g(s - 1, p + 1) or g(s // 3, p + 1) or g(s // 5, p + 1)
#         elif s % 3 == 0:
#             return g(s - 1, p + 1) or g(s // 3, p + 1) or g(s - 3, p + 1)
#         elif s % 5 == 0:
#             return g(s - 1, p + 1) or g(s - 2, p + 1) or g(s // 5, p + 1)
#         else:
#             return g(s - 1, p + 1) or g(s - 2, p + 1) or g(s - 3, p + 1)
# for S in range(18, 1000):
#     if g(S, 0):
#         print(S)

# def g(s, p):
#     if s <= 17 and p == 3:
#         return 1
#     elif s > 17 and p == 3:
#         return 0
#     elif s <= 17 and p < 3:
#         return 0
#     if p % 2 != 0:
#         if s % 3 == 0 and s % 5 == 0:
#             return g(s - 1, p + 1) and g(s // 3, p + 1) and g(s // 5, p + 1)
#         elif s % 3 == 0:
#             return g(s - 1, p + 1) and g(s // 3, p + 1) and g(s - 3, p + 1)
#         elif s % 5 == 0:
#             return g(s - 1, p + 1) and g(s - 2, p + 1) and g(s // 5, p + 1)
#         else:
#             return g(s - 1, p + 1) and g(s - 2, p + 1) and g(s - 3, p + 1)
#     else:
#         if s % 3 == 0 and s % 5 == 0:
#             return g(s - 1, p + 1) or g(s // 3, p + 1) or g(s // 5, p + 1)
#         elif s % 3 == 0:
#             return g(s - 1, p + 1) or g(s // 3, p + 1) or g(s - 3, p + 1)
#         elif s % 5 == 0:
#             return g(s - 1, p + 1) or g(s - 2, p + 1) or g(s // 5, p + 1)
#         else:
#             return g(s - 1, p + 1) or g(s - 2, p + 1) or g(s - 3, p + 1)
# for S in range(18, 1000):
#     if g(S, 0):
#         print(S)

def g(s, p):
    if s <= 17 and (p == 2 or p == 4):
        return 1
    elif s > 17 and p == 4:
        return 0
    elif s <= 17 and p < 4:
        return 0
    if p % 2 == 0:
        if s % 3 == 0 and s % 5 == 0:
            return g(s - 1, p + 1) and g(s // 3, p + 1) and g(s // 5, p + 1)
        elif s % 3 == 0:
            return g(s - 1, p + 1) and g(s // 3, p + 1) and g(s - 3, p + 1)
        elif s % 5 == 0:
            return g(s - 1, p + 1) and g(s - 2, p + 1) and g(s // 5, p + 1)
        else:
            return g(s - 1, p + 1) and g(s - 2, p + 1) and g(s - 3, p + 1)
    else:
        if s % 3 == 0 and s % 5 == 0:
            return g(s - 1, p + 1) or g(s // 3, p + 1) or g(s // 5, p + 1)
        elif s % 3 == 0:
            return g(s - 1, p + 1) or g(s // 3, p + 1) or g(s - 3, p + 1)
        elif s % 5 == 0:
            return g(s - 1, p + 1) or g(s - 2, p + 1) or g(s // 5, p + 1)
        else:
            return g(s - 1, p + 1) or g(s - 2, p + 1) or g(s - 3, p + 1)
for S in range(18, 1000):
    if g(S, 0):
        print(S)