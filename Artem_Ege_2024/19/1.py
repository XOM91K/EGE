#+1, *2, >=165, 1 <= S <= 164
#Задание 20, на одну кучу
def g(s, p):
    if (p == 2 or p == 4) and s >= 165:
        return 1
    elif p == 4 and s < 165:
        return 0
    elif p < 4 and s >= 165:
        return 0
    if p % 2 == 0:
        #Ход Пети
        return g(s + 1, p + 1) and g(s * 2, p + 1)
    else:
        #Ход Вани
        return g(s + 1, p + 1) or g(s * 2, p + 1)
for s in range(1, 165):
    if g(s, 0) == 1:
        print(s)
#82
#41 81
#80