for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R += R[-2:]
    else:
        R = '1' + R + '0'
    R = int(R, 2)
    if R == 202:
        print(N)