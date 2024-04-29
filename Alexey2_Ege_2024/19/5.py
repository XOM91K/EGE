def g(s, p):
    if (p == 4) and s >= 30:
        return 1
    elif p == 4 and s < 30:
        return 0
    elif p < 4 and s >= 30:
        return 0
    if p % 3 == 0: #Ход Кати
        return g(s + 1, p + 1) or g(s * 2, p + 1)
    if p % 3 == 1: #Ход Пети
        return g(s + 1, p + 1) or g(s * 2, p + 1)
    if p % 3 == 2: #Ход Вани
        return g(s + 1, p + 1) and g(s * 2, p + 1)
for x in range(1, 30):
    if g(x, 0):
        print(x)
#7
#13