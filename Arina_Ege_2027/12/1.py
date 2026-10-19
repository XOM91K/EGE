for x in range(1, 1000): # 1  0
    for y in range(1, 1000): # 2  1
        for z in range(1, 1000): # 0  2
            usl1 = x + y + z
            if usl1 == 1000 and x == y and (x + 2 * y) - (2 * z + y) == 178:
                print(y)