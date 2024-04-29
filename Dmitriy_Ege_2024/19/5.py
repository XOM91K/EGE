def g(s, p):
    if s >= 301 and (p == 2 or p == 4):
        return 1
    elif s < 301 and p == 4:
        return 0
    elif s >= 301:
        return 0
    if p % 2 == 0:
        return g(s + 3, p + 1) and g(s * 5, p + 1)
    else:
        return g(s + 3, p + 1) or g(s * 5, p + 1)
for x in range(1, 301):
    if g(x, 0):
        print(x)
#58