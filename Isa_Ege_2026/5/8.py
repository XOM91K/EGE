for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R += '0' * len(R)
    else:
        R += '1' * len(R)
    R = int(R, 2)
    if R < 100:
        print(R)