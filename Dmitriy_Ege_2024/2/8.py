print('x y u w')
for x in range(2):
    for y in range(2):
        for u in range(2):
            for w in range(2):
                if ((not((y <= w) == x)) and u) == 0:
                    print(x, y, u, w)