def g(s, h):
    if (h == 4 or h == 2) and s >= 108:
        return 1
    elif h == 4 and s < 108:
        return 0
    elif h < 4 and s >= 108:
        return 0
    if h % 2 == 0:
        return g(s + 1, h + 1) and g(int(s * 1.5) if s % 2 == 0 else s * 2, h + 1)
    else:
        return g(s + 1, h + 1) or g(int(s * 1.5) if s % 2 == 0 else s * 2, h + 1)
for x in range(1, 108):
    if g(x, 0):
        print(x)