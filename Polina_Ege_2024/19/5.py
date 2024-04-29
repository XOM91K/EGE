def F(x,h):
    if x >= 301 and (h == 2 or h == 4):
        return 1
    if x < 301 and h == 4:
        return 0
    if x >= 301 and h < 4:
        return 0
    if h % 2 == 0:
        return F(x + 3, h + 1) and F(x * 5, h + 1)
    else:
        return F(x + 3, h + 1) or F(x * 5, h + 1)
for x in range(1, 301):
    if F(x, 0):
        print(x)
