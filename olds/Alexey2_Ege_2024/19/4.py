def g(s1, s2, p):
    if (p == 4 or p == 2) and s1 + s2 >= 231:
        return 1
    elif p == 4 and s1 + s2 < 231:
        return 0
    elif p < 4 and s1 + s2 >= 231:
        return 0
    if p % 2 == 0:
        #Ход Пети
        return g(s1 + 2, s2, p + 1) and g(s1 * 2, s2, p + 1) and g(s1, s2 + 2, p + 1) and g(s1, s2 * 2, p + 1)
    else:
        # Ход Вани
        return g(s1 + 2, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 2, p + 1) or g(s1, s2 * 2, p + 1)
for x in range(1, 214):
    if g(17, x, 0):
        print(x)
#211
#53 105
#96