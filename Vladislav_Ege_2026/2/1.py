print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                t = (x == (w or y)) or ((w <= z) and (y <= w))
                if t == 0:
                    print(x, y, z, w)