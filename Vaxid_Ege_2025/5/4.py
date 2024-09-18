def v5(n):
    b = ''
    while n > 0:
        b += str(n % 5)
        n //= 5
    return b[::-1]
for N in range(5, 1000):
    R = v5(N)
    if N % 5 == 0:
        R = R + R[-2:]
    else:
        R = R + v5(N % 5 * 7)
    R = int(R, 5)
    if R > 200:
        print(R)