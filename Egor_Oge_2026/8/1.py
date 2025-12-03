for x in range(1, 53): # 1
    for y in range(1, 53): # 5
        for z in range(1, 53): # 4
            for w in range(1, 53): # 2
                if x + z == 52 and y + z == 30 and x + w == 47 and w + y == 25 and x + y + z + w == 77:
                    print(x, y)