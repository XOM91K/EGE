print('    x y w')
for x in range(2):
    for y in range(2):
        for w in range(2):
            if ((x and (w <= y)) == 1) == 0:
                print('0: ', x, y, w)
            else:
                print('1: ', x, y, w)