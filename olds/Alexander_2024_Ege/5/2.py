for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R += '010'
    else:
        R += bin(N % 3 * 5)[2:]
    if (int(R, 2) % 2 == 0) and (int(R, 2) > 300):
        print(N)
