for N in range(1, 1000000):
    R = bin(N)[2:]
    if N % 6 == 0:
        R = R + '111'
    else:
        R = R + '1'
    if int(R, 2) % 3 == 0:
        R = R + '101'
    else:
        R = R + '1'
    R = int(R, 2)
    if R > 300000:
        print(N)
        break