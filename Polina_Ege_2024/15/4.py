for A in range(1,300):
    k = 0
    for x in range(1,301):
        if ((A % 9 ==0 ) and ((280 % x ==0) <= ((A % x != 0) <= (730 % x != 0)))) == 1:
            k += 1
    if k == 300:
        print(A)