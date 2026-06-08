def v4(d):
    s = ''
    while d > 0:
        s += str(d % 4)
        d //= 4
    return s[::-1]
for N in range(1, 10000):
    R = v4(N)
    if R[0] == '3':
        R = R.replace('1', '!') # 1131  => !!3!
        R = R.replace('3', '1') # !!1!
        R = R.replace('!', '3')
        R = '21' + R
    else:
        R = '1' + R[1:] + '12'
    R = int(R, 4)
    if R < 598:
        print(N)