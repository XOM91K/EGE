for x in range(700):
    for y in range(700):
        for z in range(700):
            if y + z * 2 == 448 and y == z * 2:
                print(x)
