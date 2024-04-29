for N in range(1, 10000):
    R = bin(N)[2:]
    R = R + R[-1]
    R = R + str(R.count('1') % 2)
    if int(R, 2) > 105:
        print(int(R, 2))