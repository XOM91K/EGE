ct = 0
for A in range(-200, 400):
    can = True
    for x in range(-200, 400):
        for y in range(-200, 400):
            if (((A < x) or (x ** 2 - 7 * x + 10 > 0)) and ((A >= y) or (y ** 2 + 7 * y + 12 > 0))) == 0:
                can = False
                break
    if can:
        ct += 1
print(ct)