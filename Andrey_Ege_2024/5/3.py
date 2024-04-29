for N in range(9, 1000):
    d = N
    R = bin(N)[2:]
    if N % 2 == 0:
        R = R + '1'
    else:
        R = R + '0'
    N = int(R, 2)
    if N % 2 == 0:
        R = R + '1'
    else:
        R = R + '0'
    R = int(R, 2)
    if R < 171:
        print(d)