def g(s, p, hod):
    if s >= 55 and (p == 4 or p == 2):
        return 1
    elif s < 55 and p == 4:
        return 0
    elif s >= 55:
        return 0
    if p % 2 == 0:
        if hod == 0:
            return g(s + 1, p + 1, 1) and g(s + 3, p + 1, 2) and g(s * 2, p + 1, 3)
        elif hod == 1:
            return g(s + 3, p + 1, 2) and g(s * 2, p + 1, 3)
        elif hod == 2:
            return g(s + 1, p + 1, 1) and g(s * 2, p + 1, 3)
        elif hod == 3:
            return g(s + 1, p + 1, 1) and g(s + 3, p + 1, 2)

    else:
        if hod == 0:
            return g(s + 1, p + 1, 1) or g(s + 3, p + 1, 2) or g(s * 2, p + 1, 3)
        elif hod == 1:
            return g(s + 3, p + 1, 2) or g(s * 2, p + 1, 3)
        elif hod == 2:
            return g(s + 1, p + 1, 1) or g(s * 2, p + 1, 3)
        elif hod == 3:
            return g(s + 1, p + 1, 1) or g(s + 3, p + 1, 2)
for x in range(1, 55):
    if g(x, 0, 0):
        print(x)