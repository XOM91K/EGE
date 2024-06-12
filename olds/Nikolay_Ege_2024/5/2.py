for n in range(4, 1000):
    R = bin(n)[2:]
    if R.count('1') % 4 == 0:
        R = '10' + R
    else:
        R = '11' + R
    if R[-1] != '0':
        R += '0'
    else:
        R += '1'
    if int(R, 2) < 250:
        print(n)
