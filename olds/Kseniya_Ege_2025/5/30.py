for N in range(2, 10000):
    R = bin(N)[2:]
    if R.count('1') == R.count('0'):
        R += R[-1]
    else:
        if R.count('1') < R.count('0'):
            R += '1'
        else:
            R += '0'
    if R.count('1') == R.count('0'):
        R += R[-1]
    else:
        if R.count('1') < R.count('0'):
            R += '1'
        else:
            R += '0'
    if R.count('1') == R.count('0'):
        R += R[-1]
    else:
        if R.count('1') < R.count('0'):
            R += '1'
        else:
            R += '0'
    R = int(R, 2)
    if R % 7 == 0 and N > 154:
        print(N)