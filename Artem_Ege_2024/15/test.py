for A in range(1,1000):
    for x in range(1,1000):
        if ((120 % A == 0) and ((x % 36 == 0) <=((x % A != 0) <= (x % 45 != 0)))) == 0:
            break
    else:
        print(A)