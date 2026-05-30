# def g(s, p):
#     if s >= 128 and p == 2:
#         return 1
#     elif s < 128 and p == 2:
#         return 0
#     elif s >= 128 and p < 2:
#         return 0
#     if p % 2 == 0:
#         return g(s + 2, p + 1) and g(s + 5, p + 1) and g(s * 2, p + 1)
#     else:
#         return g(s + 2, p + 1) or g(s + 5, p + 1) or g(s * 2, p + 1)
# for s in range(1, 128):
#     if g(s, 0):
#         print(s)

# def g(s, p):
#     if s >= 128 and p == 3:
#         return 1
#     elif s < 128 and p == 3:
#         return 0
#     elif s >= 128 and p < 3:
#         return 0
#     if p % 2 == 0:
#         return g(s + 2, p + 1) or g(s + 5, p + 1) or g(s * 2, p + 1)
#     else:
#         return g(s + 2, p + 1) and g(s + 5, p + 1) and g(s * 2, p + 1)
# for s in range(1, 128):
#     if g(s, 0):
#         print(s)
#
#
def g(s, p):
    if s >= 128 and (p == 2 or p == 4):
        return 1
    elif s < 128 and p == 4:
        return 0
    elif s >= 128 and p < 4:
        return 0
    if p % 2 == 0:
        return g(s + 2, p + 1) and g(s + 5, p + 1) and g(s * 2, p + 1)
    else:
        return g(s + 2, p + 1) or g(s + 5, p + 1) or g(s * 2, p + 1)

for s in range(1, 128):
    if g(s, 0):
        print(s)























