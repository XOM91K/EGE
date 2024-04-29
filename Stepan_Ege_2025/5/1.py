for x in range(1000, 10000):
    x = str(x)
    sm1 = int(x[0]) + int(x[1])
    sm2 = int(x[2]) + int(x[3])
    if min(sm1, sm2) == 1 and max(sm1, sm2) == 17:
        print(x)