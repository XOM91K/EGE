#ЕСЛИ СОПЕРНИК ХОДИТ "ЛЮБЫМ ХОДОМ" ИЛИ "НЕЗАВИСИМО" ("умный ход")
# ТО ЕГО ХОДЫ БУДУТ ЧЕРЕЗ "AND"
#ЕСЛИ У СОПЕРНИКА "НЕУДАЧНЫЙ ХОД" ("глупый ход") ТО ОН ХОДИТ ЧЕРЕЗ "OR"

#У НАШЕГО ИГРОКА ХОДЫ БУДУТ ВСЕГДА ЧЕРЕЗ "OR"
def g(s, p):
    if s >= 58 and p == 3:
        return 1
    if s < 58 and p == 3:
        return 0
    if s >= 58 and p < 3:
        return 0
    if p % 2 == 0:
        return g(s + 1, p + 1) or g(s + 4, p + 1) or g(s * 2, p + 1)
    else:
        return g(s + 1, p + 1) and g(s + 4, p + 1) and g(s * 2, p + 1)
for S in range(1, 58):
    if g(S, 0):
        print(S)

