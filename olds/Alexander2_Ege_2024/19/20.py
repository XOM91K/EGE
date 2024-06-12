def g(s, p):
    if s >= 135 and p == 3:
        return 1
    elif s < 135 and p == 3:
        return 0
    elif s >= 135 and p < 3:
        return 0
    if p % 2 == 0: #ход Пети (чётные)
        #and - если соперник делает "любые ходы"
        #or - если соперник делает "неудачный ход"
        return g(s + 5, p + 1) or g(s * 3, p + 1)
    else:
        #у нашего игрока ВСЕГДА OR
        return g(s + 5, p + 1) and g(s * 3, p + 1)
for S in range(1, 135):
    if g(S, 0):
        print(S)