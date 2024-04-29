def g(s1, p):
    if s1 >= 33 and (p == 2):
        return True
    elif s1 < 33 and p == 2:
        return False
    elif s1 >= 33:
        return False
    if p % 2 == 0:
        return g(s1 + 3, p + 1) and g(s1 * 2, p + 1)
    else:
        return g(s1 + 3, p + 1) or g(s1 * 2, p + 1)
for x in range(1, 33):
    if g(x, 0):
        print(x)
#19 - 14
#20 - 5
#21 - 9, 10