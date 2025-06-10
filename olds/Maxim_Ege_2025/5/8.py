def v5(d):
    s = ''
    while d > 0:
        s += str(d % 5)
        d //= 5
    return s[::-1]
g = []
for N in range(5, 10000):
    R = v5(N)
    if N % 5 == 0:
        R += R[-2:]
    else:
        R += v5(N % 5 * 7 )
    R = int(R, 5)
    if R > 200:
        g.append(R)
print(min(g))