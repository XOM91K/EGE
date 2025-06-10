for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') > R.count('0'):
        R += '0'
    else:
        R += '11'
    R = int(R, 2)
    if R > 2019:
        print(N)

