def g(s, p):
    # s - кол-во камней в куче
    # p - ходы
    # Петя четные ходы делает
    # Ваня нечётные делает
    if s >= 627 and p == 3:
        return 1
    if s < 627 and p == 3:
        return 0
    if s >= 627 and p < 3:
        return 0
    if p % 2 != 0:
        return g(s + 3, p + 1) and g(s + 4, p + 1) and g(s ** 2, p + 1)
    else:
        return g(s + 3, p + 1) or g(s + 4, p + 1) or g(s ** 2, p + 1)
for S in range(1, 201):
    if g(S, 0):
        print(S)
