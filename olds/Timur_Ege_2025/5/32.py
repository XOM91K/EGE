for N in range(1,10000):
    R = bin(N)[2:]
    if len(R) % 2 == 0:
        R = R + '1'
    else:
        R = '1' + R + '0'
    R = int(R, 2)
    if R > 666 and R < 1030:
        print(R)