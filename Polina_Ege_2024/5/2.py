for N in range(1, 1000):
    R = int(bin(N)[2:][::-1], 2)
    if R == 13:
        print(N)

