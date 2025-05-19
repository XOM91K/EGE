def v4(d):
    s = ''
    while d > 0:
        s = str(d % 4) + s
        d //= 4
    return s
for N in range(1, 10000):
    R = v4(N)
    if len(R) % 2 == 0:
