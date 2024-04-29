for N in range(2, 10000):
    R = bin(N)[2:]
    R = R + R[-2]
    R = R + R[1]
    if int(R, 2) > 180:
        print(N)