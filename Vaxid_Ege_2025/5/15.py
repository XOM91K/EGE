def v6(d):
    s = ''
    while d > 0:
        s += str(d % 6)
        d //= 6
    return s[::-1]
d = []
for N in range(1, 10000):
    R = v6(N)
    if N % 3 == 0:
        R = R + R[:2]
    else:
        R = R + v6(N % 3 * 10)
    R = int(R, 6)
    if R > 680:
        d.append(R)
print(min(d))