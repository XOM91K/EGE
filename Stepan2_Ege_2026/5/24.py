for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = R + '11'
    else:
        R = '1' + R + '10'
    R = int(R, 2)
    if R