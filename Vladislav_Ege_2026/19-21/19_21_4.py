# def g(n, h, m):
#     if (n + h) >= 123 and m == 2:
#         return 1
#     elif (n + h) < 123 and m == 2:
#         return 0
#     elif (n + h) >= 123 and m < 2:
#         return 0
#     if m % 2 == 0:
#         return g(n + 1, h, m + 1) or g(n * 2, h, m + 1) or g(n, h + 1, m + 1) or g(n, h * 2, m + 1)
#     if m % 2 != 0:
#         return g(n + 1, h, m + 1) or g(n * 2, h, m + 1) or g(n, h + 1, m + 1) or g(n, h * 2, m + 1)
#
#
# for S in range(1, 110):
#     if g(13, S, 0):
#         print(S)

# def g(n, h, m):
#     if (n + h) >= 123 and m == 3:
#         return 1
#     elif (n + h) < 123 and m == 3:
#         return 0
#     elif (n + h) >= 123 and m < 3:
#         return 0
#     if m % 2 == 0:
#         return g(n + 1, h, m + 1) or g(n * 2, h, m + 1) or g(n, h + 1, m + 1) or g(n, h * 2, m + 1)
#     if m % 2 != 0:
#         return g(n + 1, h, m + 1) and g(n * 2, h, m + 1) and g(n, h + 1, m + 1) and g(n, h * 2, m + 1)
#
#
# for S in range(1, 110):
#     if g(13, S, 0):
#         print(S)

def g(n, h, m):
    if (n + h) >= 123 and (m == 2 or m == 4):
        return 1
    elif (n + h) < 123 and m == 4:
        return 0
    elif (n + h) >= 123 and m < 4:
        return 0
    if m % 2 == 0:
        return g(n + 1, h, m + 1) and g(n * 2, h, m + 1) and g(n, h + 1, m + 1) and g(n, h * 2, m + 1)
    if m % 2 != 0:
        return g(n + 1, h, m + 1) or g(n * 2, h, m + 1) or g(n, h + 1, m + 1) or g(n, h * 2, m + 1)


for S in range(1, 110):
    if g(13, S, 0):
        print(S)
