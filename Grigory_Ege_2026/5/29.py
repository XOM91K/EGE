for N in range(1, 1000):
    R = bin(N)[2:]
    if N % 4 == 0:
        R += R[:2]
    else:
        R += bin((N % 4) + 1)[2:]
    R = int(R, 2)
    if R >= 50:
        print(N)
