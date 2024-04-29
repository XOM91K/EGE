for N in range(1, 1000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R += '00'
    else:
        R += '11'
    if int(R, 2) > 115:
        print(N)