for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') == R.count('0'):
        R = R + R[-1]
    else:
        if R.count('1') < R.count('0'):
            R = R + '1'
        else:
            R = R + '0'
    if R.count('1') == R.count('0'):
        R = R + R[-1]
    else:
        if R.count('1') < R.count('0'):
            R = R + '1'
        else:
            R = R + '0'
    if R.count('1') == R.count('0'):
        R = R + R[-1]
    else:
        if R.count('1') < R.count('0'):
            R = R + '1'
        else:
            R = R + '0'
    R = int(R,2)
    if N > 154 and R % 7 == 0:
        print(N)