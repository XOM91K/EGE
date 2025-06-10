for x in range(1000, 10000):
    x = str(x)
    sm1 = int(x[0]) + int(x[1])
    sm2 = int(x[1]) + int(x[2])
    sm3 = int(x[2]) + int(x[3])
    if max(sm1, sm2, sm3) == 15 and sm1 + sm2 + sm3 - max(sm1, sm2, sm3) - min(sm1, sm2, sm3) == 15:
        print(x)