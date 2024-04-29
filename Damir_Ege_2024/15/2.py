for A in range(1, 1000):
    ok = True
    for x in range(1, 1000):
        if ((A % 45 == 0) and ((750 % x == 0) <= ((A % x != 0) <= (120 % x != 0)))) == 0:
            ok = False
            break
    if ok:
        print(A)