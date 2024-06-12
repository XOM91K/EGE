#На полякове №5375
#Задача №21 (вопрос 3)
def g(s, p):
    if (p == 2 or p == 4) and s >= 165:
        return 1
    elif p == 4 and s < 165:
        return 0
    elif p < 4 and s >= 165:
        return 0
    # and - умные ходы (любые ходы)
    # or - глупые ходы (неудачные ходы)
    # наш игрок ВСЕГДА ХОДИТ "OR"
    if p % 2 == 0: #Ход Пети при p % 2 == 0
        return g(s + 1, p + 1) and g(s * 2, p + 1)
    else: #Ход Вани при p % 2 != 0
        return g(s + 1, p + 1) or g(s * 2, p + 1)
for x in range(1, 165):
    if g(x, 0):
        print(x)
#82
#41 81
#80