def pt(d):
    s = ''
    while d > 0:
        s += str(d % 5)
        d //= 5
    return s[::-1]
for N in range(1, 100000):
    R = pt(N)
    R = R[::-1]
    R = int(R, 5) - N
    if R == 100:
        print(N)