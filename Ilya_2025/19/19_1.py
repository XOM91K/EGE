def g(s, p):
    if p == 2 and s >= 68:
        return 1
    elif p == 2 and s < 68:
        return 0
    elif p < 2 and s >= 68:
        return 0
    if p % 2 == 0:
        # or - у соперника тогда, когда он делает неудачный ход
        # and - у соперника тогда, когда он делает  "Любой ход", , "независимо"
        return g(s + 1, p + 1) or g(s + 4, p + 1) or g(s * 5, p + 1)
    else:
        #у нашего игрока всегда ходы через OR
        return g(s + 1, p + 1) or g(s + 4, p + 1) or g(s * 5, p + 1)
for S in range(1, 68):
    if g(S, 0) == 1:
        print(S)