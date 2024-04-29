def g(s1, s2, p):
    if s1 + s2 >= 259 and (p == 2 or p == 4):
        return True
    if s1 + s2 < 259 and p == 4:
        return False
    if s1 + s2 >= 259 and p < 4:
        return False
    if p % 2 == 0:
        #П
        return g(s1 + 1, s2, p + 1) and g(s1 * 2, s2, p + 1) and g(s1, s2 + 1, p + 1) and g(s1, s2 * 2, p + 1)
    else:
        #В
        return g(s1 + 1, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 1, p + 1) or g(s1, s2 * 2, p + 1)
for s in range(1, 242):
    if g(17, s, 0) == True:
        print(s)
#61
#------
#112
#120
#