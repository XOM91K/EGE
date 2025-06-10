def f(n):
    s = ''
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s
for N in range(1, 10000):
    R = f(N)
    if len(R) % 2 == 0:
        # 312023
        R = R[:len(R) // 2] + '0' + R[len(R) // 2 + 1:]
    if int(R) <= 180:
        print(N)