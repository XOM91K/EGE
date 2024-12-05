#У Нашего игрока всегда будут ходы ВСЕГДА через "OR"
#У Соперника ходы через "And" если он ходит "умно" (независимо, любой ход)
#У Соперника ходы через "or" если он ходит "глупо" (неудачный ход)
def g(s, p):
    if s >= 82 and p == 2:
        return 1
    elif s < 82 and p == 2:
        return 0
    elif s >= 82 and p < 2:
        return 0
    if p % 2 == 0:
        return g(s + 2, p + 1) or g(s + 4, p + 1) or g(s * 3, p + 1)
    else:
        return g(s + 2, p + 1) or g(s + 4, p + 1) or g(s * 3, p + 1)
for S in range(1, 82):
    if g(S, 0):
        print(S)