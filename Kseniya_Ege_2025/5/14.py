
for N in range(1, 10000):
    R = bin(N)[2:]
    R = R.replace('1', 'x')
    R = R.replace('0', '1')
    R = R.replace('x', '0')
    if R.count('1') % 2 == 0:
        R = R + '0'
    else:
        R = R + '1'
    R = int(R, 2)
    if R < 170:
        print(R)