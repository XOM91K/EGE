# def g(s1, s2, p):
#     if (s1 + s2) >= 212 and p == 3:
#         return 1
#     if (s1 + s2)  < 212 and p == 3:
#         return 0
#     if (s1 + s2)  >= 212 and p < 3:
#         return 0
#
#     if p%2 == 0:
#         return g(s1 + s2, s2, p + 1) or g(s1, s2 + s1, p + 1)
#     else:
#         return g(s1 + s2, s2, p + 1) and g(s1, s2 + s1, p + 1)
# for S in range(0, 112):
#     if g(50, S, 0):
#         print(S)

def g(s1, s2, p):
    if (s1 + s2) >= 212 and (p == 4):
        return 1
    if (s1 + s2) < 212 and p == 4:
        return 0
    if (s1 + s2) >= 212 and p < 4:
        return 0

    if p % 2 == 0:
        return g(s1 + s2, s2, p + 1) and g(s1, s2 + s1, p + 1)
    else:
        return g(s1 + s2, s2, p + 1) or g(s1, s2 + s1, p + 1)


for S in range(0, 112):
    if g(10, S, 0):
        print(S)
