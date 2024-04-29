for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R += '0'
    else:
        R += '1'
    if N % 2 == 0:
        R += '1'
    else:
        R += '0'
    R = int(R, 2)
    if R > 204:
        print(R, N)