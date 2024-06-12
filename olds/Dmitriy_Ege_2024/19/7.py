def g(x, y, h):
    if (h == 4 or h == 2) and x + y >= 231:
        return 1
    elif h == 4 and x + y < 231:
        return 0
    elif h < 4 and x + y >= 231:
        return 0
    if h % 2 == 0:
        return g(x + 4, y, h + 1) and g(x * 3, y, h + 1) and g(x, y + 4, h + 1) and g(x, y * 3, h + 1)
    else:
        return g(x + 4, y, h + 1) or g(x * 3, y, h + 1) or g(x, y + 4, h + 1) or g(x, y * 3, h + 1)
for x in range(1, 218):
    if g(x, 10, 0) == 1:
        print(x)
#62
# 67
# 68
# 70