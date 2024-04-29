print('   x', 'y', 'w', 'z')
for x in range(0, 2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                if (((x <= y) or (z <= w)) and (not (x <= w))) == 1:
                    print('1:', x, y, w, z)
                else:
                    print('0:', x, y, w, z)
