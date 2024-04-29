for x in range(10000, 100000):
    x = str(x)
    sm1 = int(x[0]) + int(x[2]) + int(x[4])
    sm2 = int(x[1]) + int(x[3])
    if sm1 == 23 and sm2 == 7:
        print(x)