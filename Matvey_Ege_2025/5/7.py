def v3(x):
    s = ''
    while x > 0:
        s += str(x % 3)
        x //= 3
    return s[::-1]
l = []
for N in range(1, 10000):
    R = v3(N)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += v3(sum(map(int, R)))
    R = int(R, 3)
    if R > 278 and R % 2 != 0:
        l.append(R)
print(min(l))