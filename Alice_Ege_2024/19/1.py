def g(s, p):
    if s >= 59 and (p == 2 or p == 4):
        return True
    if s < 59 and p == 4:
        return False
    if s >= 59 and p < 4:
        return False
    #Наш соперник всегда ходит "and", потому что он делает "любой ход"
    #У нашего игрока всегда будут ходы через "or"
    if p % 2 == 0:
        #Ход Пети
        return g(s + 1, p + 1) and g(s + 4, p + 1) and g(s * 3, p + 1)
    else:
        #Ход Вани
        return g(s + 1, p + 1) or g(s + 4, p + 1) or g(s * 3, p + 1)
for x in range(1, 59):
    if g(x, 0) == True:
        print(x)
#19
#15, 18