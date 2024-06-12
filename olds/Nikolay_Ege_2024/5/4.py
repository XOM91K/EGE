def tr(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s
mx = 10 ** 10
for N in range(11, 10000):
    R = tr(N)
    if R.count('0') + R.count('2') > R.count('1'):
        R = '22' + R
    else:
        R = '11' + R
    R = int(R, 3)
    if R > 100:
        print(R)
