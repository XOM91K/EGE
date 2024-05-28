def g(s1, s2, p):
    if p == 4 and s1 + s2 >= 212:
        return True
    if p == 4 and s1 + s2 < 212:
        return False
    if p < 4 and s1 + s2 >= 212:
        return False
    if p % 2 == 0:
        #ход Пети
        return g(s1 + s2, s2,  p + 1) and g(s1, s1 + s2,  p + 1)
    else:
        #ход Вани
        return g(s1 + s2, s2,  p + 1) or g(s1, s1 + s2,  p + 1)
for x in range(112):
    if g(10, x, 0) == True:
        print(x)