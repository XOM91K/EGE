def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]

for N in range(1, 10000):
    R = v3(N)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += v3(N % 3 * 5)
    R = int(R, 3)
    if R > 133:
        print(R)