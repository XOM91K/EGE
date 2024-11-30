for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') > R.count('0'):
        