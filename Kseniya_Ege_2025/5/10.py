for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R = '1' + R + '00'
    else:
        R = '11' + R
    R = int(R, 2)
    if R >= 412:
        print(N)
