def g(s, p):
    if s >= 56 and p == 2:
        return 1
    elif s < 56 and p == 2:
        return 0
    elif s >= 56 and p < 2:
        return 0
    #ПРОТИВНИК ЕСЛИ ХОДИТ НЕУДАЧНЫМ ХОДОМ, ТО МЫ СТАВИМ "or"
    #ПРОТИВНИК ЕСЛИ ХОДИТ ЛЮБЫМ ХОДОМ (УМНЫМ), ТО МЫ СТАВИМ "and"
    #НАШИ ХОДЫ (НАШЕГО ИГРОКА) ВСЕГДА БУДУТ ЧЕРЕЗ "or"
    if p % 2 == 0:
        if s % 3 == 0:
            return g(s + 1, p + 1) or g(s + 2, p + 1) or g(s * 3, p + 1)
        else:
            return g(s + 1, p + 1) or g(s + 2, p + 1)
    else:
        if s % 3 == 0:
            return g(s + 1, p + 1) or g(s + 2, p + 1) or g(s * 3, p + 1)
        else:
            return g(s + 1, p + 1) or g(s + 2, p + 1)
for S in range(1, 56):
    if g(S, 0):
        print(S)