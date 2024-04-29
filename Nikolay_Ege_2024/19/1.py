def g(s, p):
    if p == 2 and s >= 165:
        return 1
    elif p == 2 and s < 165:
        return 0
    elif p < 2 and s >= 165:
        return 0
    #любой ход соперника - "and"
    #неудачный ход соперника - "or"
    #наш игрок (ход игрока, который выгирывает) - "or"
    if p % 2 == 0:
        return g(s + 1, p + 1) and g(s * 2, p + 1)
    else:
        return g(s + 1, p + 1) or g(s * 2, p + 1)
for x in range(1, 165):
    if g(x, 0) == 1:
        print(x)
#82
#41, 81
#81