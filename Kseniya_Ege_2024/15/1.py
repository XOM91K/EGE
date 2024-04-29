for A in range(1, 1000):
    c = 1
    for x in range(1, 1000):
        if ((A + x < 123) <= ((x % 5 == 0) <= (x % 7 != 0))) == 0:
            c = 0
            break
    if c:
        print(A)