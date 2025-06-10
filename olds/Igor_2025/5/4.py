def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
d = []
for N in range(1, 10000):
    R = v3(N)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += v3(sum([int(x) for x in R]))
    R = int(R, 3)
    if R > 220 and R % 2 == 0:
        print(R)
        d.append(R)
print(min(d))