for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 4 == 0:
        R = '1' + '1' if R[-1] == '0' else '0'
    else:
        R = '1' + R + '1'
    R = int(R, 2)
    if R > 100:
        print(N)