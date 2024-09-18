#Даниэль
for A in range(0, 500):
    can = True
    for x in range(0, 500):
        for y in range(0, 500):
            if ((11 * x - y != 53) or (x > y) or (A < x)) == 0:
                can = False
    if can:
        print(A)