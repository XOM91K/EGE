def v5(n):
    s = ''
    while n > 0:
        s += str( n % 5 )
        n //= 5
    return s[::-1]
for N in range(1, 10000):
    R = v5(N)
    if int(R[-1]) % 2 == 0:
        R = R + '2'
    else:
        R = '2' + R + '3'
    R = int(R, 5)
    if R < 1000:
        print(N)