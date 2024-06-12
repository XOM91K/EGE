def g(s1, s2, p):
    if p == 2 and s1 + s2 >= 77:
        return True
    if p == 2 and s1 + s2 < 77:
        return False
    if p < 2 and s1 + s2 >= 77:
        return False
    if p % 2 == 0:
        #ход Пети
        return g(s1 + 1, s2,  p + 1) or g(s1 * 2, s2,  p + 1) or g(s1, s2 + 1,  p + 1) or g(s1, s2 * 2, p + 1)
    else:
        #ход Вани
        return g(s1 + 1, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 1, p + 1) or g(s1, s2 * 2, p + 1)
for x in range(1, 70):
    if g(7, x, 0) == True:
        print(x)
