for N in range(1, 10000):
    R = bin(N)[2:]
    R += R[-1] #10101010
    R += % 2
    print(N, R)