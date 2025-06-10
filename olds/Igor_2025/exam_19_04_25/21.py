def g(s, p):
    # s - кучка
    # p - № хода
    # Чётные - ХОДИТ Петя
    # Нечётные - ХОДИТ Ваня
    if s >= 128 and p % 2 == 0:
        return 1
    if (s >= 128 and p%2 != 0) or p > 4:
        return 0
    else:
        if p%2!=0:
            return g(s+2, p+1) or g(s+5, p+1) or g(s*2, p+1)
        else:
            return g(s+2, p+1) and g(s+5, p+1) and g(s*2, p+1)

for S in range(1, 127+1):
    if g(S, 0):
        print(S)