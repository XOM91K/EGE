for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R= R + '11'
    else:
        R = R + '01'
    R = int(R, 2)
    if R > 61:
        print(R)