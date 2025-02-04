def v3(a):
    s = ''
    while a > 0:
        s += str(a % 3)
        a //= 3
    return s[::-1]
for N in range(11, 10000):
    R = v3(N)
    if R.count('0') + R.count('2') > R.count('1'):
        R = '22' + R
    else:
        R = '11' + R
    R = int(R, 3)
    if R > 100:
        print(R)
