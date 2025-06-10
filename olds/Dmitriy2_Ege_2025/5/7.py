for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R = R + R[-2:]
    else:
        d = R[-2:]
        d = d.replace('0', '#')
        d = d.replace('1', '0')
        d = d.replace('#', '1')
        R = R + d
    R = int(R, 2)
    if R > 154:
        print(N)
# R = '10101010'
# R = R + R[-2:]
# print(R)