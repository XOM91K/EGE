def g(s, p):
    if s >= 68 and p == 2:
        return 1
    if s < 68 and p == 2:
        return 0
    if s >= 68 and p < 2:
        return 0
    # у нашего игрока ходы ВСЕГДА через OR
    # у соперника ходы:
    # AND - если ходит умно (любой, независимый ход)
    # OR - если ходит глупо (неудачный ход)
    if p % 2 == 0:
        return g(s + 1, p + 1) or g(s + 4, p + 1) or g(s * 5, p + 1)
    else:
        return g(s + 1, p + 1) or g(s + 4, p + 1) or g(s * 5, p + 1)
for S in range(1, 68):
    if g(S, 0):
        print(S)