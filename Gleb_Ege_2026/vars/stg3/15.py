n = 100000
for A in range(0, n):
    can = True
    for x in range(1, n):
        for y in range(1, n):
            if ((y < A) and (x < A) or (89241 < 5 * y + x)) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)
        break