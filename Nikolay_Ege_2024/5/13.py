def v4(n):
    s = ''
    while n > 0:
        s += str(n % 4)
        n //= 4
    return s[::-1]
for N in range(1, 1000):
    R = v4(N)
    R = str(N % 2) + R + str(N % 3)
    R = int(R, 4)
    if len(str(R)) == 2:
        print(R)