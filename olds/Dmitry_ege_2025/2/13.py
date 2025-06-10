print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((z == (not x)) <= ((w <= (not y)) and (y <= x))) == 1:
                    print(x, y, z, w)