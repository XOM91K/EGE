# def g(s, p):
#     if s >= 172 and p == 2:
#         return 1
#     elif s < 172 and p == 2:
#         return 0
#     elif s >= 172 and p < 2:
#         return 0
#
#     if p % 2 == 0:
#         return g(s + 1, p + 1) and g(s + 2, p + 1) and g(s + 3, p + 1) and g(s * 2, p + 1)
#     else:
#         return g(s + 1, p + 1) or g(s + 2, p + 1) or g(s + 3, p + 1) or g(s * 2, p + 1)
# for S in range(1, 172):
#     if g(S, 0):
#         print(S)
# def g(s, p):
#     if s >= 172 and p == 3:
#         return 1
#     elif s < 172 and p == 3:
#         return 0
#     elif s >= 172 and p < 3:
#         return 0
#
#     if p % 2 == 0:
#         return g(s + 1, p + 1) or g(s + 2, p + 1) or g(s + 3, p + 1) or g(s * 2, p + 1)
#     else:
#         return g(s + 1, p + 1) and g(s + 2, p + 1) and g(s + 3, p + 1) and g(s * 2, p + 1)
# for S in range(1, 172):
#     if g(S, 0):
#         print(S)
def g(s, p):
    if s >= 172 and (p == 2 or p == 4):
        return 1
    elif s < 172 and p == 4:
        return 0
    elif s >= 172 and p < 4:
        return 0

    if p % 2 == 0:
        return g(s + 1, p + 1) and g(s + 2, p + 1) and g(s + 3, p + 1) and g(s * 2, p + 1)
    else:
        return g(s + 1, p + 1) or g(s + 2, p + 1) or g(s + 3, p + 1) or g(s * 2, p + 1)
for S in range(1, 172):
    if g(S, 0):
        print(S)

# Петя всегда ходит первым через проверку p % 2 == 0
# Соперник ходит всегда через AND
# Наш игрок всегда ходит через OR
# в 19 задании наш игрок это Ваня
# в 20 наш игрок это Петя
# в 21 наш игрок это Ваня