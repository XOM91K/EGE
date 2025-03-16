def v8(d):
    s = ''
    while d > 0:
        s += str(d % 8)
        d //= 8
    return s[::-1]
for N in range(1, 1000):
    R = v8(N)
    if N % 5 == 0:
        R = R + R[:3]
    else:
        R = R + str(bin(N % 5)[2:])
    R = int(R, 8)
    if R >= 35000:
        print(N)