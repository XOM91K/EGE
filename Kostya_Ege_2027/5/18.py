def v4(d):
    s = ''
    while d > 0:
        s += str(d % 4)
        d //= 4
    if s == '':
        return '0'
    return s[::-1]
d = []
for N in range(1, 100000):
    R = v4(N)
    if N % 2 == 0:
        R = '12' + R + v4(int(R[-1]) * 3)
    else:
        R = '13' + R + '21'
    R = int(R, 4)
    if R > 50:
        print(R)
        d.append(R)
print(min(d))