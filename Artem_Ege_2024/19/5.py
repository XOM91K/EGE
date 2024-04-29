def g(s, p):
    if s > 29 and (p == 4):
        return 1
    elif s <= 29 and p == 4:
        return 0
    elif s > 29 and p < 4:
        return 0
    if p % 3 == 0:
        return g(s + 1, p + 1) or g(s * 2, p + 1)
    if p % 3 == 1:
        return g(s + 1, p + 1) or g(s * 2, p + 1)
    if p % 3 == 2:
        return g(s + 1, p + 1) and g(s * 2, p + 1)
ct = 0
for x in range(1, 30):
    if g(x, 0):
        print(x)
        ct += 1
print('ct:',ct)