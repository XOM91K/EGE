# def g(s1, s2, p):
#     if s1 * s2 >= 541 and p == 2:
#         return 1
#     elif s1 * s2 < 541 and p == 2:
#         return 0
#     elif s1 * s2 >= 541 and p < 2:
#         return 0
#     if p % 2 == 0:
#         return g(s1 + 10, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 10, p + 1) or g(s1, s2  * 2, p + 1)
#     else:
#         return g(s1 + 10, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 10, p + 1) or g(s1, s2 * 2, p + 1)
# for S in range(1, 501):
#     if g(6, S, 0):
#         print(S)

# def g(s1, s2, p):
#     if s1 * s2 >= 541 and p == 3:
#         return 1
#     elif s1 * s2 < 541 and p == 3:
#         return 0
#     elif s1 * s2 >= 541 and p < 3:
#         return 0
#     if p % 2 == 0:
#         return g(s1 + 10, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 10, p + 1) or g(s1, s2  * 2, p + 1)
#     else:
#         return g(s1 + 10, s2, p + 1) and g(s1 * 2, s2, p + 1) and g(s1, s2 + 10, p + 1) and g(s1, s2 * 2, p + 1)
# for S in range(1, 501):
#     if g(6, S, 0):
#         print(S)

def g(s1, s2, p):
    if s1 * s2 >= 541 and (p == 2 or p == 4):
        return 1
    elif s1 * s2 < 541 and p == 2:
        return 0
    elif s1 * s2 >= 541 and p < 4:
        return 0
    if p % 2 != 0:
        return g(s1 + 10, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 10, p + 1) or g(s1, s2  * 2, p + 1)
    else:
        return g(s1 + 10, s2, p + 1) and g(s1 * 2, s2, p + 1) and g(s1, s2 + 10, p + 1) and g(s1, s2 * 2, p + 1)
for S in range(1, 501):
    if g(6, S, 0):
        print(S)