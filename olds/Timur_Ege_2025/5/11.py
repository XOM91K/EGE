
for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 5 == 0:
        R = R[:3] + R
    else:
        R = R + bin(N % 5 * 5)[2:]
    R = int(R, 2)
    if N % 2 != 0 and R < 313:
        print(N)