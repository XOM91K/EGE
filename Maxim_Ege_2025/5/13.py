for N in range(155,1000):
    R = bin(N)[2:]
    if R.count('1') == R.count('0'):
        R = R+R[-1] # 100
    else:
        if R.count('1') > R.count('0'):
            R =  R + '0'
        if R.count('1') < R.count('0'):
            R = R + '1'
    if R.count('1') == R.count('0'):
        R = R + R[-1]  # 100
    else:
        if R.count('1') > R.count('0'):
            R = R + '0'
        if R.count('1') < R.count('0'):
            R = R + '1'
    if R.count('1') == R.count('0'):
        R = R + R[-1]  # 100
    else:
        if R.count('1') > R.count('0'):
            R = R + '0'
        if R.count('1') < R.count('0'):
            R = R + '1'
    R = int(R,2)
    if R%7==0:
        print(N)