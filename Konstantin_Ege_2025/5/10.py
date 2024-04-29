def f5(d):
    s = ''
    while d > 0:
        s += str(d % 5)
        d //= 5
    return s[::-1]
for N in range(1, 10000):
    R = f5(N)
    R = R[::-1]
    R = abs(N - int(R, 5))
    if R == 100:
        print(N)