for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') > R.count('0'):
        R = R + '1'
    else:
        R = R + '0'
    R = int(R, 2)
    if R < 90:
        print(R)