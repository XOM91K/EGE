print('# x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x <= y) or (z == x)) and (w <= z)) == 0:
                    print(0, x, y, z, w)