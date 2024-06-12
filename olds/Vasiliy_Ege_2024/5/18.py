def v5(n):
    s = ''
    while n > 0:
        s += str(n % 5)
        n = n // 5
    return s[::-1]


for n in range(1, 10000):
    R = v5(n)
    if n % 25 == 0:
        R = R[-3:] + R
    else:
        R = R + (v5(n % 25))
    if int(R, 5) > 10000:
        print(n)