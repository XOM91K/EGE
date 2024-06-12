def tr(N):
    s = ''
    while N > 0:
        s = str(N % 3) + s
        N //= 3
    return s
for x in range(1, 1000):
    R = tr(x) #101010210201
    if sum(map(int, R)) % 3 == 0:
        R = '20' + R
    else:
        R = '10' + R
    R = int(R, 3)
    if R < 100:
        print(x)


