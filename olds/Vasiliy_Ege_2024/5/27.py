def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n = n // 3
    return s[::-1]


for x in range(0, 1000):
    c = v3(x)
    if (c.count('1') + c.count('2') * 2) % 2 == 0:
        c = '2' + v3(x)[2:] + '0'
    else:
        c = '20' + v3(x)[2:] + '1'
    if int(c, 3) > 75:
        print(x, int(c, 3))