for N in range(10000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = '1' + R + '0'
    else:
        R = '11' + R + '11'
    if int(R, 2) > 52:
        print(int(R, 2))