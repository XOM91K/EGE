print("x,y,w,z")
for x in range(0,2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                if ((w <= (y == z)) and (y ==(z <= x))) == 0:
                    print(x, y, w, z)