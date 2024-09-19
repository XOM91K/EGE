for A in range(0, 300):
    can = True
    for x in range(0, 300):
        for y in range(0, 300):
            if (((x > 68) or (y > 89)) or (2 * x - 7 * y < A)) == 0:
                can = False
    if can:
        print(A) 
        break