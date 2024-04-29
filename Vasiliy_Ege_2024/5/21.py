def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n = n // 3
    return s[::-1]


for a in range(1, 10000):
    R = v3(a)
    if a % 2 == 0:
        R = '1' + R + '00'
    else:
        R = R + v3(R.count('1') + R.count('2') * 2)
    if int(R, 3) > 168:
        print(a)
        break