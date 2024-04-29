for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R += R[-2:]
    else:
        R = '1' + R + '0'
    if int(R, 2) < 100:
        print(N)