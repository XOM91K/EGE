for N in range(1, 1000):
    R = bin(N)[2:]
    if R.count('1') > R.count('0'):
        R = R + '0'
    else:
        R = R + '11'
    R = int(R, 2)
    if R > 2019:
        print(N)