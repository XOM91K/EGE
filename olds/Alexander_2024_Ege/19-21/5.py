def g(s1, s2, h):
    if h == 1 and ((s1 >= 65) or (s2 >= 65)):
        return 1
    elif h == 1 and not((s1 >= 65) or (s2 >= 65)):
        return 0
    elif h < 1 and ((s1 >= 65) or (s2 >= 65)):
        return 0
    if h % 2 == 0:
        if s1 > s2:
            return g(s1 + 1, s2, h + 1) or g(s1 + 2, s2, h + 1) or g(s1 + 3, s2, h + 1) or g(s1, s2 * 2, h + 1)
        elif s1 == s2:
            return g(s1 + 1, s2, h + 1) or g(s1 + 2, s2, h + 1) or g(s1 + 3, s2, h + 1)
        else:
            return g(s1, s2 + 1, h + 1) or g(s1, s2 + 2, h + 1) or g(s1, s2 + 3, h + 1) or g(s1 * 2, s2, h + 1)
    else:
        if s1 > s2:
            return g(s1 + 1, s2, h + 1) and g(s1 + 2, s2, h + 1) and g(s1 + 3, s2, h + 1) and g(s1, s2 * 2, h + 1)
        elif s1 == s2:
            return g(s1 + 1, s2, h + 1) and g(s1 + 2, s2, h + 1) and g(s1 + 3, s2, h + 1)
        else:
            return g(s1, s2 + 1, h + 1) and g(s1, s2 + 2, h + 1) and g(s1, s2 + 3, h + 1) and g(s1 * 2, s2, h + 1)
mx = 10 ** 10
for s11 in range(1, 100):
    for s22 in range(1, 100):
        if g(s11, s22, 0):
            mx = min(mx, s11 + s22)
print(mx)