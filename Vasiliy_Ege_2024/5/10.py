for N in range(105, 10000):
    R = bin(N)[2:]
    if R.count('1') == R.count('0'):
        R = R + R[-1]
    else:
        if R.count('1') > R.count('0'):
            R = R + '0'
        else:
            R = R + '1'
    if R.count('1') == R.count('0'):
        R = R + R[-1]
    else:
        if R.count('1') > R.count('0'):
            R = R + '0'
        else:
            R = R + '1'
    if R.count('1') == R.count('0'):
        R = R + R[-1]
    else:
        if R.count('1') > R.count('0'):
            R = R + '0'
        else:
            R = R + '1'
    if int(R, 2) % 4 == 0:
        print(N)

