for x in range(1000, 10000):
    sm1 = int(str(x)[0]) + int(str(x)[1])
    sm2 = int(str(x)[1]) + int(str(x)[2])
    sm3 = int(str(x)[2]) + int(str(x)[3])
    if max(sm1, sm2, sm3) == 17 and (sm1 + sm2 + sm3) - max(sm1, sm2, sm3) - min(sm1, sm2, sm3) == 15:
        print(x)