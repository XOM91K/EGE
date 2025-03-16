for N in range(1, 1000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R = R + R[-2:]
    else:
        g = R[-2:]
        g = g.replace('0', '#')
        g = g.replace('1', '0')
        g = g.replace('#', '1')
        R = R + g
    R = int(R, 2)
    if int(R) > 154:
        print(N)
