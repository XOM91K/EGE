print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((z == (not y)) and ((not x) or y) and w) == 1:
                    print(x, y, z, w)