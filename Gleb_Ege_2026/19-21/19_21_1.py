# def g(s1, s2, p):
#     if (s1 >= 78 or s2 >= 78) and p == 1:
#         return 1
#     elif (not(s1 >= 78 or s2 >= 78)) and p == 1:
#         return 0
#     elif (s1 >= 78 or s2 >= 78) and p < 1:
#         return 0
#     if p % 2 == 0:
#         if s1 > s2:
#             return g(s1 + 1, s2, p + 1) or g(s1 + 2, s2, p + 1) or g(s1 + 3, s2, p + 1) or g(s1, s2 * 2, p + 1)
#         elif s1 == s2:
#             return g(s1 + 1, s2, p + 1) or g(s1 + 2, s2, p + 1) or g(s1 + 3, s2, p + 1)
#         else:
#             return g(s1 * 2, s2, p + 1) or g(s1, s2 + 2, p + 1) or g(s1, s2 + 1, p + 1) or g(s1, s2 + 3, p + 1)
#
#     else:
#         if s1 > s2:
#             return g(s1 + 1, s2, p + 1) or g(s1 + 2, s2, p + 1) or g(s1 + 3, s2, p + 1) or g(s1, s2 * 2, p + 1)
#         elif s1 == s2:
#             return g(s1 + 1, s2, p + 1) or g(s1 + 2, s2, p + 1) or g(s1 + 3, s2, p + 1)
#         else:
#             return g(s1 * 2, s2, p + 1) or g(s1, s2 + 2, p + 1) or g(s1, s2 + 1, p + 1) or g(s1, s2 + 3, p + 1)
# s = []
# for s1 in range(1, 100):
#     for s2 in range(1, 100):
#         if g(s1, s2, 0):
#             s.append(s1 + s2)
# print(min(s))
def g(s1, s2, p):
    if (s1 >= 78 or s2 >= 78) and (p == 2 or p == 4):
        return 1
    elif (not(s1 >= 78 or s2 >= 78)) and p == 4:
        return 0
    elif (s1 >= 78 or s2 >= 78) and p < 4:
        return 0
    if p % 2 != 0:
        if s1 > s2:
            return g(s1 + 1, s2, p + 1) or g(s1 + 2, s2, p + 1) or g(s1 + 3, s2, p + 1) or g(s1, s2 * 2, p + 1)
        elif s1 == s2:
            return g(s1 + 1, s2, p + 1) or g(s1 + 2, s2, p + 1) or g(s1 + 3, s2, p + 1)
        else:
            return g(s1 * 2, s2, p + 1) or g(s1, s2 + 2, p + 1) or g(s1, s2 + 1, p + 1) or g(s1, s2 + 3, p + 1)

    else:
        if s1 > s2:
            return g(s1 + 1, s2, p + 1) and g(s1 + 2, s2, p + 1) and g(s1 + 3, s2, p + 1) and g(s1, s2 * 2, p + 1)
        elif s1 == s2:
            return g(s1 + 1, s2, p + 1) and g(s1 + 2, s2, p + 1) and g(s1 + 3, s2, p + 1)
        else:
            return g(s1 * 2, s2, p + 1) and g(s1, s2 + 2, p + 1) and g(s1, s2 + 1, p + 1) and g(s1, s2 + 3, p + 1)
s = []
for s1 in range(1, 78):
    #for s2 in range(1, 100):
        if g(69, s1, 0):
            print(s1)