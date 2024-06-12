print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (w and ((not x) or y) and ((not y) and z or y and (not z))) == 1:
                    print(x, y, z, w)