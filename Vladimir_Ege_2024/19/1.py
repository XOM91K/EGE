#1 куча, +1 +3 *4, >=111
#S = ? 1 <= S <= 110    [20, 21]
#Задача №21 (3-й вопрос)
def g(s, p):
    if (p == 2 or p == 4) and s >= 111:
        return 1
    elif p == 4 and s < 111:
        return 0
    elif p < 4 and s >= 111:
        return 0
    if p % 2 == 0:
        #ход Пети
        return g(s + 1, p + 1) and g(s + 3, p + 1) and g(s * 4, p + 1)
    else:
        #ход Вани
        return g(s + 1, p + 1) or g(s + 3, p + 1) or g(s * 4, p + 1)
for s in range(1, 111):
    if g(s, 0):
        print(s)

#27
#24 26
#23