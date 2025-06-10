for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 1:
        R = R + '11'
    else:
        R = '11' + R
    R = int(R, 2)
    if R > 102:
        print(N)