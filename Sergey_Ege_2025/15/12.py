for A in range(0, 300):
    can = True
    for x in range(0, 300):
        for y in range(0, 300):
            if ((x + y <= 30) or (y <= x + 2) or (y >= A)) == 0:
                can = False
    if can:
        print(A)