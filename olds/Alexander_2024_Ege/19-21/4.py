def g(s1, s2, h):
    if (h == 2 or h == 4) and s1 + s2 >= 123:
        return 1
    elif h == 2 and s1 + s2 < 123:
        return 0
    elif h < 4 and s1 + s2 >= 123:
        return 0
    if h % 2 == 0:
        #Ход Пети
        return g(s1 + 2, s2, h + 1) or g(s1 * 2, s2, h + 1) or g(s1, s2 + 2, h + 1) or g(s1, s2 * 2, h + 1)
    else:
        #Ход Вани
        return g(s1 + 2, s2, h + 1) or g(s1 * 2, s2, h + 1) or g(s1, s2 + 2, h + 1) or g(s1, s2 * 2, h + 1)


for x in range(1, 41):
    if g(3, x, 0):
        print(x)
#40
#57 58
#56