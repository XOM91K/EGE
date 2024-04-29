def g(x, y, h):
    if x + y >= 123 and (h == 2 or h == 4):
        return 1
    elif x + y < 123 and h == 4:
        return 0
    elif x + y >= 123 and h < 4:
        return 0
    if h % 2 != 0:
        return g(x + 1, y, h + 1) or g(x, y + 1, h + 1) or g(x * 2, y, h + 1) or g(x, y * 2, h + 1)
    else:
        return g(x + 1, y, h + 1) and g(x, y + 1, h + 1) and g(x * 2, y, h + 1) and g(x, y * 2, h + 1)
for x in range(1, 110):
    if g(13, x, 0):
        print(x)