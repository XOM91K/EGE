d = 100
for a in range(d, 1, -1):
    can = True
    for x in range(1, d):
        for y in range(1, d):
            if (((9*x + y) > a) or (x >= 36) or (y >= 18)) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(a)
        break