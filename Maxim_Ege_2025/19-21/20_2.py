def g(s, p):
    if s >= 435 and p == 3:
        return 1
    elif s < 435 and p == 3:
        return 0
    elif s >= 435 and p < 3:
        return 0
    if p % 2 == 0:
        return g(s + 5, p + 1) or g(s * 3, p + 1)
    else:
        return g(s + 5, p + 1) and g(s * 3, p + 1)
for x in range(1, 435):
    if g(x, 0):
        print(x)
#140
#47 48