print("   x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((z <= w) <= (not y)) and x) == 1:
                    print('1:', x,y,z,w)
print("   x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((z <= w) <= (not y)) and x) == 0:
                    print('0:', x, y, z, w)