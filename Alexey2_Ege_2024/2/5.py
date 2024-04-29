print('n x,y,w,z')
for x in range(0,2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                if ((not(x <= (not(z <= w)))) and ((not z) <= ((not w) == y))) == 1:
                    print(1, x,y,w,z)
                if ((not(x <= (not(z <= w)))) and ((not z) <= ((not w) == y))) == 0:
                    print(0, x,y,w,z)