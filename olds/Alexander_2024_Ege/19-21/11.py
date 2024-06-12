def g(s, p):
    if s >= 132 and p == 3:
        return 1
    elif s < 132 and p == 3:
        return 0
    elif s >= 132:
        return 0
    if p % 2 != 0:
        if s % 2 == 0 and s % 3 == 0:
            return g(s + 1, p + 1) and g(s + s // 2, p + 1) and g(s + s // 3, p + 1)
        elif s % 2 == 0 and s % 3 != 0:
            return g(s + 1, p + 1) and g(s + s // 2, p + 1)
        elif s % 2 != 0 and s % 3 == 0:
            return g(s + 1, p + 1) and g(s + s // 3, p + 1)
        else:
            return g(s + 1, p + 1) and g(s * 2, p + 1)
    else:
        if s % 2 == 0 and s % 3 == 0:
            return g(s + 1, p + 1) or g(s + s // 2, p + 1) or g(s + s // 3, p + 1)
        elif s % 2 == 0 and s % 3 != 0:
            return g(s + 1, p + 1) or g(s + s // 2, p + 1)
        elif s % 2 != 0 and s % 3 == 0:
            return g(s + 1, p + 1) or g(s + s // 3, p + 1)
        else:
            return g(s + 1, p + 1) or g(s * 2, p + 1)
for S in range(1, 132):
    if g(S, 0):
        print(S)
#48
#62 68