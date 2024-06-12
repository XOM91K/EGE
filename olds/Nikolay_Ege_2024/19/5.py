def g(s1, s2, p):
    if (p == 2 or p==4) and (s1 < 10 or s2 < 10):
        return 1
    elif p == 4  and (s1 >= 10 and s2 >= 10):
        return 0
    elif p < 4 and (s1 < 10 or s2 < 10):
        return 0
    if p % 2 == 0:  # Ход Пети
        return g(s1 - 1, s2, p + 1) and g(s1, s2 - 1, p + 1) and g(s1 - 3, s2, p + 1) and g(s1, s2 - 3, p + 1)
    else:
        return g(s1 - 1, s2, p + 1) or g(s1, s2 - 1, p + 1) or g(s1 - 3, s2, p + 1) or g(s1, s2 - 3, p + 1)

for x in range(100, 10, -1):
    if g(13, x, 0):
        print(x)
# любой ход соперника - "and"
# неудачный ход соперника - "or"
# наш игрок (ход игрока, который выгирывает) - "or"