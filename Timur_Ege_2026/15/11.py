n = 100000
for A in range(78122, n):
    can = True
    for x in range(1, n):
        for y in range(1, n):
            if ((78125 != y + 4 * x) or ((A > x) and (A > y))) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)