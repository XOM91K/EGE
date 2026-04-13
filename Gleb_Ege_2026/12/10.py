for y in range(1001): #1 -> 0
    for x in range(1001 - y): #0 -> 2 0.336
        for z in range(1001 - x - y): #2 -> 1
            if z + x + y == 1000 and x * 2 + z == 448 and z == x * 2:
                print(y)