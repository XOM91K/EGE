
for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ( ((x >= A) or (121>= x**2)) and ((y**2 < 49) or (A < y) ) ) ==0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)