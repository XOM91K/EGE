for x in range(100, 1000):
    x = str(x)
    sm1 = int(x[0]) + int(x[1])
    sm2 = int(x[1]) + int(x[2])
    if max(sm1, sm2) == 14 and min(sm1, sm2) == 12:
        print(x)