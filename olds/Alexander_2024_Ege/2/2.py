print('   x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = (x == y) and (w <= z)
                f2 = (x <= y) <= (w == z)
                if f1 == 1 and f2 == 0:
                    print('1:', x, y, z, w)
                if f1 == 1:
                    print('2:', x, y, z, w)
                if f1 == 0 and f2 == 0:
                    print('3:', x, y, z, w)