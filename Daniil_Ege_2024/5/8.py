for N in range(1, 10000):
    R = bin(N)[2:]
    ed = R.count('1')
    if N % 2 == 0:
        R = R + '0'
    else:
        R = R + '1'
    if ed % 2 == 0:
        R = R + '0'
    else:
        R = R + '1'
    R = int(R, 2)
    print(R)