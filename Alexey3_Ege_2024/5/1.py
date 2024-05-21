def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
mn = 10 ** 10
for N in range(1, 10000):
    R = v3(N)
    if N % 7 == 0:
        R += R[-2:]
    else:
        R += v3(N % 7 * 3)
    R = int(R, 3)
    if R > 369:
        mn = min(mn, R)
print(mn)