def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n = n // 3
    return s[::-1]


for a in range(1, 10000):
    R = v3(a) #01201
    if (R.count('1') + R.count('2') * 2) % 3 == 0:
        R = '20' + R
    else:
        R = '10' + R
    R = int(R, 3)
    if R < 100:
        print(a)