for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = R + R[-3:]
    else:
        R = R + bin(N % 3 * 3)[2:]
    R = int(R, 2)
    if R < 170:
        print(R)