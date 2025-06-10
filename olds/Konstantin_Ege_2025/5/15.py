for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 1:
        R += '1'
    else:
        R += '0'
    if R.count('1') % 2 == 1:
        R += '1'
    else:
        R += '0'
    R = int(R, 2)
    if R < 86:
        print(N)