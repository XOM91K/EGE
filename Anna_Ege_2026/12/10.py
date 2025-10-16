for x in range(1001): # 0
    for y in range(1001): # 1
        for z in range(1001): # 2
            if y > 2 * z and (x * 2 + z) - (y + z * 2) == 1640:
                print(x)
