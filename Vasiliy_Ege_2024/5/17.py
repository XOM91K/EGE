for x in range(0, 10000):
    R = oct(x)[2:]
    c = str(int(R, 8))
    if c.count('1') % 2 == 0:
        R = R + str(x % 3)
    else:
        R = max(R) + R
    if int(R, 8) > 127:
        print(x, int(R, 8))