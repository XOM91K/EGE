for A in range(1, 10000):
    for x in range(1, 10000):
        if ((A + x < 123) <= ((x % 5 == 0) <= (x % 7 != 0))) == 1:
            print(A)