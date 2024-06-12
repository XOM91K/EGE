for N in range(1, 10000):
    R = bin(N)[2:]
    R += R[-1]
    R += str(R.count('1') % 2)
    R = int(R, 2)
    if R > 105:
        print(R)