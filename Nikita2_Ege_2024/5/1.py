for N in range(1, 10000):
    R = bin(N)[2:] #1011
    R += str(R.count('1') % 2)
    R += str(R.count('1') % 2)
    if int(R, 2) > 43:
        print(int(R, 2))