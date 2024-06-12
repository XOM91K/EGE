print('   x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x and y) or ((z == y) and w)) == 0:
                    print('0:', x, y, z, w)
                else:
                    print('1:', x, y, z, w)