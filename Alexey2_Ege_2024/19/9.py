#https://kompege.ru/variant?kim=25037848
def g(s, p):
    if (p == 2 or p == 4) and s <= 12:
        return 1
    elif p == 4 and s > 12:
        return 0
    elif p < 4 and s <= 12:
        return 0
    if p % 2 == 0:
        if s % 2 == 0:
            return g(s - 1, p + 1) and g(s // 2, p + 1)
        else:
            return g(s - 1, p + 1)
    else:
        if s % 2 == 0:
            return g(s - 1, p + 1) or g(s // 2, p + 1)
        else:
            return g(s - 1, p + 1)
for S in range(13, 100):
    if g(S, 0):
        print(S)
