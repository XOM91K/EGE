for N in range(1, 1000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = '10' + R + '1'
    else:
        R = '1' + R + '01'
    if int(R, 2) > 420:
        print(N)