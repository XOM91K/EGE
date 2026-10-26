for N in range(1, 10000):
    R = bin(N)[2:]
    if '0' in R:
        x = R.rindex('0')
        R = R[:x] + R[:2] + R[x + 1:]
        R = R[::-1]
        R = int(R, 2)
        if R == 123:
            print(N)