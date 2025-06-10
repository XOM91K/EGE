for N in range(1, 100):
    R = bin(N)[2:]
    R = R[::-1]
    if int(R, 2) == 13:
        print(N)
