def F(s, p):
    if s >= 129 and (p == 2 or p == 4):
        return 1
    elif s < 129 and p == 4:
        return 0
    elif s >= 129 and p < 4:
        return 0
    if p % 2 == 0:
        #Ход Пети
        return F(s + 1, p + 1) and F(s * 2, p + 1)
    else:
        #Ход Вани
        return F(s + 1, p + 1) or F(s * 2, p + 1)
for x in range(129):
    if F(x, 0):
        print(x)