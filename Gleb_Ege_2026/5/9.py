for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 5 == 0:
        R = R + R[:3]
    else:
        R = R + bin((N % 5) * 5)[2:]
    R = int(R, 2)
    if R < 313:
        print(N)