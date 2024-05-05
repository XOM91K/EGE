for N in range(0, 1000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = R + R[-2:]
    else:
        R = '1' + R + '0'
    if int(R, 2) == 202:
        print(N)