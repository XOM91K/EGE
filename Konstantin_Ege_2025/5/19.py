def v3(d):
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    return s[::-1]
d = []
for N in range(11, 10000):
    R = v3(N)
    if R.count('0') + R.count('2') > R.count('1'):
        R = '22' + R
    else:
        R = '11' + R
    R = int(R, 3)
    if R > 100:
        d.append(R)
print(min(d))