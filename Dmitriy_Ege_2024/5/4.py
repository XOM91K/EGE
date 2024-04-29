for N in range(1, 1000):
    R = bin(N)[2:]
    if R.count('1') % 4 == 0:
        R = '10' + R
    else:
        R = '11' + R
    if R[-1] == '0':
        R += '1'
    else:
        R += '0'
    if int(R, 2) <= 250:
        print(N)