for N in range(1, 10000):
    R = bin(N)[2:]
    R += str(R.count('1') % 2)
    R += str(R.count('1') % 2)
    R = int(R, 2)
    if R < 86:
        print(N)