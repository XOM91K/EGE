for N in range(1, 10000):
    R = bin(N)[2:]
    R = R[::-1]
    R = R + R[-1]
    R = int(R, 2)
    if R > 99:
        print(N)