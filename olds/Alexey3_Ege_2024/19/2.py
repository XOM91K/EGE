def f(s, p):
    if p == 3 and s >= 435:
        return 1
    elif p == 3 and s < 435:
        return 0
    elif p < 3 and s >= 435:
        return 0
    if p % 2 == 0:
        #если "любой ход" у соперника то and
        #если "неудачный" у соперника то or
        return f(s + 5, p + 1) or f(s * 3, p + 1)
    else:
        #ходы нашего игрока всегда OR
        return f(s + 5, p + 1) and f(s * 3, p + 1)
for S in range(1, 435):
    if f(S, 0):
        print(S)