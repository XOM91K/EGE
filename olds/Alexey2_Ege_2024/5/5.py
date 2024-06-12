def fo(d):
    s = ''
    while d > 0:
        s += str(d % 4)
        d //= 4
    return s[::-1]
mx = 0
for N in range(1, 10000):
    R = fo(N)
    R = str(N % 2) + R
    R = R + str(N % 3)
    if len(str(int(R, 4))) == 2:
        mx = max(mx, int(R, 4))
print(mx)