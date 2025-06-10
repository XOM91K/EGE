for A in range(1, 1000):
    k = 0
    for x in range(1, 1000):
        if ((A + x < 123) <= ((x % 5 == 0) <= (x % 7 != 0))) == 1:
            k += 1
    if k == 999:
        print(A)