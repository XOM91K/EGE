for N in range(1, 1000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = R + '10'
    else:
        R = '1' + R + '00'
    R = int(R, 2)
    if R > 107:
        print(N)