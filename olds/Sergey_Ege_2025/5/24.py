def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
for N in range(4, 10000):
    R = v3(N)
    if R[-2:] == '10':
        R = '2' + R
    else:
        R = '1' + R
    R = int(R, 3)
    if R > 130:
        print(N)