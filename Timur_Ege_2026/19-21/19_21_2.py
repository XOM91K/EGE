# def g(s, p):
#     if s >= 39 and p == 2:
#         return True
#     if s < 39 and p == 2:
#         return False
#     if s >= 39 and p < 2:
#         return False
#
#     if p % 2 == 0:
#         return g(s + 1, p + 1) and g(s + 3, p + 1) and g(s * 2, p + 1)
#     else:
#         return g(s + 1, p + 1) or g(s + 3, p + 1) or g(s * 2, p + 1)
# for S in range(1, 39):
#     if g(S, 0):
#         print(S)
# def g(s, p):
#     if s >= 39 and p == 3:
#         return True
#     if s < 39 and p == 3:
#         return False
#     if s >= 39 and p < 3:
#         return False
#
#     if p % 2 == 0:
#         return g(s + 1, p + 1) or g(s + 3, p + 1) or g(s * 2, p + 1)
#     else:
#         return g(s + 1, p + 1) and g(s + 3, p + 1) and g(s * 2, p + 1)
#     # НАШ ИГРОК всегда ходит OR
#     # НАШ СОПЕРНИК ПОЧТИ ВСЕГДА ХОДИТ AND
# for S in range(1, 39):
#     if g(S, 0):
#         print(S)

def g(s, p):
    if s >= 39 and (p == 2 or p == 4):
        return True
    if s < 39 and p == 4:
        return False
    if s >= 39 and p < 4:
        return False

    if p % 2 == 0:
        return g(s + 1, p + 1) and g(s + 3, p + 1) and g(s * 2, p + 1)
    else:
        return g(s + 1, p + 1) or g(s + 3, p + 1) or g(s * 2, p + 1)
    # НАШ ИГРОК всегда ходит OR
    # НАШ СОПЕРНИК ПОЧТИ ВСЕГДА ХОДИТ AND
for S in range(1, 39):
    if g(S, 0):
        print(S)