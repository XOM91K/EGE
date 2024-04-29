for N in range(1, 1000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = R + R[-2] + R[-1]
    else:
        R = '1' + R + '0'
    if int(R, 2) < 100:
        print(N)