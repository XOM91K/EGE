for N in range(2, 10000):
    R = bin(N)[2:]
    R = R[:-1]
    if N % 2 != 0:
        R += '10'
    else:
        R += '01'
    if int(R, 2) == 2017:
        print(N)
