# 1000
for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R = R + R[-2:]
    else:
        R = R + R[-2:].replace('0', '#').replace('1', '0').replace('#', '1')
    R = int(R, 2)
    if R > 154:
        print(N)