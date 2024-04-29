#>=259 +1 *2 [17, S] 1<=S<=241
def g(s1, s2, p):
    if (p == 2 or p == 4) and s1 + s2 >= 259:
        return 1
    elif p == 4 and s1 + s2 < 259:
        return 0
    elif p < 4 and s1 + s2 >= 259:
        return 0
    if p % 2 == 0:
        #Ход Пети
        return g(s1 + 1, s2, p + 1) and g(s1 * 2, s2, p + 1) and g(s1, s2 + 1, p + 1) and g(s1, s2 * 2, p + 1)
    else:
        #Ход Вани
        return g(s1 + 1, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 1, p + 1) or g(s1, s2 * 2, p + 1)
for S in range(1, 242):
    if g(17, S, 0):
        print(S)