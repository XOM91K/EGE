for N in range(11, 10000):
    R = oct(N)[2:]
    if N % 5 == 0:
        R = R + R[0:3]
    else:
        R = R + bin(N % 5)[2:]
    if int(R, 8) >= 35000:
        print(N)
        break