for N in range(1, 10000):
    R = bin(N)[2:]
    for x in range(2):
        R += str(sum(map(int, R)) % 2)
    R = int(R, 2)
    if R > 253:
        print(N)
        break