for N in range(1, 10000):
    R = bin(N)[2:]
    R += str(R.count('1') % 2)
    R += str(R.count('1') % 2)
    if int(R, 2) > 137:
        print(N)