for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R += '0'
    else:
        R += '1'
    if bin(N)[2:].count('1') % 2 == 0:
        R += '0'
    else:
        R += '1'
    if int(R, 2) > 2023:
        print(int(R, 2))