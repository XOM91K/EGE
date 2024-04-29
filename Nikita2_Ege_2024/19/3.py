#21 задание
def g(s, p):
    if s >= 33 and (p == 2 or p == 4):
        return 1
    elif s < 33 and p == 4:
        return 0
    elif s >= 33 and p < 4:
        return 0
    if p % 2 == 0:
        return g(s + 3, p + 1) and g(s * 2, p + 1)
    else:
        return g(s + 3, p + 1) or g(s * 2, p + 1)
for x in range(1, 33):
    if g(x, 0) == 1:
        print(x)
#14
#5
#9 10