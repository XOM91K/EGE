def v3(d):
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    return s[::-1]
g = []
for N in range(1, 10000):
    R = v3(N)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += v3(sum(map(int, R)))
    R = int(R, 3)
    if R > 278 and R % 2 != 0:
        g.append(R)
print(min(g))