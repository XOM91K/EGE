def v4(x):
    s = ''
    while x > 0:
        s += str(x % 4)
        x //= 4
    return s[::-1]
for N in range(1, 10000):
    R = v4(N)
    if sum(map(int, R)) % 2 == 0:
        # 1102301
        # 13 + 02301 + '0
        R = '13' + R[2:] + '0'
        #R = R[:2] == 13 + R + '0'
    else:
        R = '2' + R[:-2] + '13'
       # R = '2' + R + R[-2:] == 13
    R = int(R, 4)
    if R == 167:
        print(N)