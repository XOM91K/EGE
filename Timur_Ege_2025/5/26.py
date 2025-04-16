def v3(a):
    s = ''
    while a > 0:
        s += str(a % 3)
        a //= 3
    return s[::-1]
for N in range(4,10000):
    R = v3(N)
    if R[-2:] == '10':
        R = '2' + R
    else:
        R = '1' + R
    R = int(R, 3)
    if R > 130:
        print(N)