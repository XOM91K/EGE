#19 задача
# def g(s, p):
#     if s >= 82 and p == 2:
#         return 1
#     elif s < 82 and p == 2:
#         return 0
#     elif s >= 82 and p < 2:
#         return 0
#     if p % 2 == 0:
#         return g(s + 2, p + 1) or g(s + 4, p + 1) or g(s * 3, p + 1)
#     else:
#         return g(s + 2, p + 1) or g(s + 4, p + 1) or g(s * 3, p + 1)
# for S in range(1, 82):
#     if g(S, 0) == 1:
#         print(S)

#20 задача
# def g(s, p):
#     if s >= 82 and p == 3:
#         return 1
#     elif s < 82 and p == 3:
#         return 0
#     elif s >= 82 and p < 3:
#         return 0
#     if p % 2 == 0:
#         return g(s + 2, p + 1) or g(s + 4, p + 1) or g(s * 3, p + 1)
#     else:
#         return g(s + 2, p + 1) and g(s + 4, p + 1) and g(s * 3, p + 1)
# for S in range(1, 82):
#     if g(S, 0) == 1:
#         print(S)

#21
def g(s, p):
    if s >= 82 and (p == 2 or p == 4):
        return 1
    elif s < 82 and p == 4:
        return 0
    elif s >= 82 and p < 4:
        return 0
    if p % 2 == 0:
        return g(s + 2, p + 1) and g(s + 4, p + 1) and g(s * 3, p + 1)
    else:
        return g(s + 2, p + 1) or g(s + 4, p + 1) or g(s * 3, p + 1)
for S in range(1, 82):
    if g(S, 0) == 1:
        print(S)