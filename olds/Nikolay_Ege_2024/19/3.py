#6647 на полякове
def g(s1, s2, p): #21 задача
    #s1 - первая куча
    #s2 - вторая куча
    #p - отслеживатель ходов
    if s1 * s2 >= 123 and (p == 2 or p == 4):
        return 1
    elif s1 * s2 < 123 and p == 4: #тут нужно потом поменять на p == 2, чтобы исключить числа полученные при втором ходе
        return 0
    elif s1 * s2 >= 123 and p < 4:
        return 0
    if p % 2 == 0: #ход Пети
        return g(s1 + 2, s2, p + 1) and g(s1 * 2, s2, p + 1) and g(s1, s2 + 2, p + 1) and g(s1, s2 * 2, p + 1)
    else: #ход Вани
        return g(s1 + 2, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 2, p + 1) or g(s1, s2 * 2, p + 1)
for x in range(1, 41):
    if g(3, x, 0):
        print(x)
#38
#17 18
#16