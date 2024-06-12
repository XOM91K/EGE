def tr(d):
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    s = s[::-1]
    return s
for n in range(3,1000):
    R= tr(n)
    if n % 2 == 0:
        R = '1' + R + '00'
    else:
        R += tr(R.count('1') + R.count('2') * 2)
    if int(R, 3) > 168:
        print(n)