#Даниэль, №1127
for A in range(1, 1001):
    can = True
    for x in range(1, 1001):
        if ((A % 7 == 0) and ((240 % x == 0) <= ((A % x != 0) <= (780 % x != 0)))) == 0:
            can = False
    if can == True:
        print(A)