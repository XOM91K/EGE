for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = R + '0'
    else:
        R = R + '1'
    if bin(N)[2:].count('1') % 2 == 0:
        R = R + '0'
    else:
        R = R + '1'
    R = int(R, 2)
    if R > 2023:
        print(R)