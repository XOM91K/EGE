for N in range(1, 10000):
    R = bin(N)[2:] #1000 + '0'
    R = R + R[-1]
    R += str(R.count('1') % 2)
    print(int(R, 2))