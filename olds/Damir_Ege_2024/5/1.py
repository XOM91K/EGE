for N in range(1, 1000):
    R = bin(N)[2:]
    R += str(R.count('1') % 2)
    R += str(R.count('1') % 2)
    if int(R, 2) > 97:
        print(int(R, 2))