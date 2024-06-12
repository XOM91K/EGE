for N in range(1, 1000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R += '10'
    else:
        R += '01'
    R = int(R, 2)
    if R < 109:
        print(R)

