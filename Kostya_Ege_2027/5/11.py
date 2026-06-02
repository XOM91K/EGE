def v5(d):
    s = ''
    while d > 0:
        s += str(d % 5)
        d //= 5
    return s[::-1]

d = []
for N in range(5, 1000):
    R = v5(N)
    if N % 5 == 0:
        R = R + R[-2:]
    if N % 5 != 0:
        R = R + v5((N % 5) * 7)
    R = int(R, 5)
    if R > 200:
        d.append(R)
print(min(d))