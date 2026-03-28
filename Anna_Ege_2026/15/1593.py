for a in range(0, 1000):
    can = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((y > a)or (152 != 2*y + 3*x) or (a<x)) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(a)