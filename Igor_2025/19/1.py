def g(s, p):
    #s - количество камней в куче
    #p - отслеживатель ходов
    #изначально при вызове функции p = 0
    #при каждом ходе игрока, игрок p + 1
    if p == 2 and s >= 68:
        return 1
    elif (p == 2 and s < 68) or s >= 68:
        return 0
    #у нашего игрока ходы всегда через or
    #у соперника, если делает неудачный ход то "or", а если любой ход или независимый то "and"
    if p % 2 == 0:
        return g(s + 1, p + 1) or g(s + 4, p + 1) or g(s * 5, p + 1)
    return g(s + 1, p + 1) or g(s + 4, p + 1) or g(s * 5, p + 1)
for S in range(1, 68):
    if g(S, 0):
        print(S)