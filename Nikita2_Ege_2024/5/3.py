for N in range(1, 1000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = R + '10'
    else:
        R = R + '01'
    if int(R, 2) < 109:
        print(int(R, 2))